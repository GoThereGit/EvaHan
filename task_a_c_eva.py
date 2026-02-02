import json
from typing import Dict, List, Tuple, Set

def calculate_edit_operations(ref: str, hyp: str) -> Tuple[int, int, int, int]:
    """
    Compute the edit distance between the reference text and the predicted text, and decompose the operation types：
    :param ref: reference text (authentic label)
    :param hyp: predictive text (OCR output)
    :return:  (editor's distance, deletions (missing characters), insertions (extra characters), replacements (incorrect characters))
    """
    m = len(ref)
    n = len(hyp)
    
    # DP Table: Each element stores (minimum distance, number of deletions, number of insertions, number of replacements)
    dp = [[(0, 0, 0, 0) for _ in range(n + 1)] for __ in range(m + 1)]
    
    for j in range(n + 1):
        dp[0][j] = (j, 0, j, 0)

    for i in range(m + 1):
        dp[i][0] = (i, i, 0, 0)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ref[i-1] == hyp[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Character mismatch; select the operation with the lowest cost (delete/insert/replace).
                del_dist, del_del, del_ins, del_rep = dp[i-1][j]
                ins_dist, ins_del, ins_ins, ins_rep = dp[i][j-1]
                rep_dist, rep_del, rep_ins, rep_rep = dp[i-1][j-1]
                
                del_total = del_dist + 1
                ins_total = ins_dist + 1
                rep_total = rep_dist + 1
                
                min_total = min(del_total, ins_total, rep_total)
                if min_total == del_total:
                    dp[i][j] = (del_total, del_del + 1, del_ins, del_rep)
                elif min_total == ins_total:
                    dp[i][j] = (ins_total, ins_del, ins_ins + 1, ins_rep)
                else:
                    dp[i][j] = (rep_total, rep_del, rep_ins, rep_rep + 1)
    
    return dp[m][n]

def calculate_char_metrics(ref: str, hyp: str) -> Dict:
    """
    Calculate all character-level metrics for a single sample: CER, accuracy, recall, F1 score, NED
    :param ref: reference text
    :param hyp: predictive text
    :return: dictionary containing all indicators
    """
    ref_len = len(ref)
    hyp_len = len(hyp)
    edit_dist, del_num, ins_num, rep_num = calculate_edit_operations(ref, hyp)
    
    # 1. CER
    if ref_len == 0:
        cer = 1.0 if hyp_len > 0 else 0.0
    else:
        cer = edit_dist / ref_len
    
    # 2. correct character count
    correct_chars = max(0, ref_len - del_num - rep_num)
    
    # 3. precision
    if hyp_len == 0:
        precision = 0.0 if ref_len > 0 else 1.0
    else:
        precision = correct_chars / hyp_len
    
    # 4. recall
    if ref_len == 0:
        recall = 0.0 if hyp_len > 0 else 1.0
    else:
        recall = correct_chars / ref_len
    
    # 5. F1-Score
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    
    # 6. NED
    max_len = max(ref_len, hyp_len)
    if max_len == 0:
        ned = 0.0
    else:
        ned = edit_dist / max_len
    
    # 7. comprehensive score
    comprehensive_score = (1 - cer) * 0.5 + f1 * 0.3 + (1 - ned) * 0.2
    
    return {
        "cer": round(cer, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "ned": round(ned, 4),
        "comprehensive_score": round(comprehensive_score, 4),
        "edit_distance": edit_dist,
        "correct_chars": correct_chars,
        "missing_chars": del_num,
        "extra_chars": ins_num,
        "wrong_chars": rep_num
    }

def load_json_to_dict(json_path: str) -> Dict[str, str]:
    """
    Read the JSON file and convert it into a dictionary with the format {image_path: text}.
    :param json_path: JSON file path (format:[{"image_path": "...", "text": "..."}])
    :return: Image-to-text mapping dictionary
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File does not exist:{json_path}")
    except json.JSONDecodeError:
        raise ValueError(f"JSON format error:{json_path}")
    
    # Validate Data Format
    if not isinstance(data, list):
        raise ValueError(f"The JSON file should be in array format, currently as follows:{type(data)}")
    
    result_dict = {}
    duplicate_images: Set[str] = set()
    for idx, sample in enumerate(data):
        if not isinstance(sample, dict) or "image_path" not in sample or "text" not in sample:
            raise ValueError(f"The {idx+1}th data entry has a format error and must include the image_path and text fields:{sample}")
        
        img_path = sample["image_path"]
        text = sample["text"]
        
        # Detect duplicate image paths
        if img_path in result_dict:
            duplicate_images.add(img_path)
            print(f"The image path {img_path} appears multiple times within {json_path}. Retrieve the text from the last occurrence.")
        
        result_dict[img_path] = text
    
    if duplicate_images:
        print(f"Note: {len(duplicate_images)} duplicate image paths detected: {list(duplicate_images)}")
    
    return result_dict

def evaluate_ocr(ref_json_path: str, pred_json_path: str) -> Dict:
    """
    Batch Evaluation of OCR Results (Reference/Prediction Both in Identical JSON Format)
    :param ref_json_path: reference data JSON file path
    :param pred_json_path: path to the prediction data JSON file
    :return: Overall Evaluation Results (including all metrics, error statistics, and sample details)
    """

    print(f"Reading reference data:{ref_json_path}")
    ref_dict = load_json_to_dict(ref_json_path)
    print(f"Reading prediction data:{pred_json_path}")
    pred_dict = load_json_to_dict(pred_json_path)
    
    # Verify sample matching
    ref_images = set(ref_dict.keys())
    pred_images = set(pred_dict.keys())
    
    # Images present in the reference file but absent in the prediction file
    missing_in_pred = ref_images - pred_images
    if missing_in_pred:
        print(f"Warning: {len(missing_in_pred)} reference images are missing in the prediction file. This is treated as an empty prediction.")
        print(f"Missing List (Top 10):{list(missing_in_pred)[:10]}")
    
    # Images present in the prediction file but absent in the reference file
    extra_in_pred = pred_images - ref_images
    if extra_in_pred:
        print(f"Note: {len(extra_in_pred)} predicted images are not in the reference set and will be ignored:")
        print(f"Redundant List (Top 10):{list(extra_in_pred)[:10]}")
    
    # Initialize statistical variables
    total_samples = len(ref_images)
    total_cer = 0.0
    total_precision = 0.0
    total_recall = 0.0
    total_f1 = 0.0
    total_ned = 0.0
    total_comprehensive = 0.0
    total_edit_dist = 0
    total_correct = 0
    total_missing = 0
    total_extra = 0
    total_wrong = 0
    total_ref_chars = 0
    total_hyp_chars = 0
    sample_details = []
    
    for img_path in ref_images:
        ref_text = ref_dict[img_path]
        hyp_text = pred_dict.get(img_path, "")  # Missing predictions are treated as empty text.
        
        metrics = calculate_char_metrics(ref_text, hyp_text)
        
        total_cer += metrics["cer"]
        total_precision += metrics["precision"]
        total_recall += metrics["recall"]
        total_f1 += metrics["f1"]
        total_ned += metrics["ned"]
        total_comprehensive += metrics["comprehensive_score"]
        total_edit_dist += metrics["edit_distance"]
        total_correct += metrics["correct_chars"]
        total_missing += metrics["missing_chars"]
        total_extra += metrics["extra_chars"]
        total_wrong += metrics["wrong_chars"]
        total_ref_chars += len(ref_text)
        total_hyp_chars += len(hyp_text)
        
        sample_details.append({
            "image": img_path,
            "ref_text": ref_text,
            "pred_text": hyp_text,
            "ref_length": len(ref_text),
            "pred_length": len(hyp_text),
            "correct_chars": metrics["correct_chars"],
            "cer": metrics["cer"],
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1": metrics["f1"],
            "ned": metrics["ned"],
            "comprehensive_score": metrics["comprehensive_score"],
            "missing_chars": metrics["missing_chars"],
            "extra_chars": metrics["extra_chars"],
            "wrong_chars": metrics["wrong_chars"],
            "edit_distance": metrics["edit_distance"]
        })
    
    # Calculate the overall metric (average value)
    overall_metrics = {
        "overall_cer": round(total_cer / total_samples, 4) if total_samples > 0 else 0.0,
        "overall_precision": round(total_precision / total_samples, 4) if total_samples > 0 else 0.0,
        "overall_recall": round(total_recall / total_samples, 4) if total_samples > 0 else 0.0,
        "overall_f1": round(total_f1 / total_samples, 4) if total_samples > 0 else 0.0,
        "overall_ned": round(total_ned / total_samples, 4) if total_samples > 0 else 0.0,
        "overall_comprehensive_score": round(total_comprehensive / total_samples, 4) if total_samples > 0 else 0.0,
        "total_samples": total_samples,
        "total_ref_chars": total_ref_chars,
        "total_hyp_chars": total_hyp_chars,
        "total_correct_chars": total_correct,
        "total_edit_distance": total_edit_dist
    }
    
    # Error Statistics
    total_errors = total_missing + total_extra + total_wrong
    error_stats = {
        "total_missing": total_missing,
        "total_extra": total_extra,
        "total_wrong": total_wrong,
        "missing_ratio": round(total_missing / total_errors, 4) if total_errors > 0 else 0.0,
        "extra_ratio": round(total_extra / total_errors, 4) if total_errors > 0 else 0.0,
        "wrong_ratio": round(total_wrong / total_errors, 4) if total_errors > 0 else 0.0
    }
    
    # Data Validation Information
    data_check = {
        "ref_sample_count": len(ref_images),
        "pred_sample_count": len(pred_images),
        "missing_in_pred": len(missing_in_pred),
        "extra_in_pred": len(extra_in_pred),
        "matched_sample_count": len(ref_images & pred_images)
    }
    
    # Final outcome
    eval_result = {
        "data_check": data_check,
        "overall_metrics": overall_metrics,
        "error_statistics": error_stats,
        "sample_details": sample_details
    }
    
    return eval_result

def print_eval_result(eval_result: Dict):
    """Formatted Print Evaluation Report"""
    print("\n" + "="*80)
    print("                    Comprehensive Evaluation Report on OCR for Ancient Texts                    ")
    print("="*80)
    
    data_check = eval_result["data_check"]
    print(f"\n[1. Data Validation]")
    print(f"├─ Reference sample size: {data_check['ref_sample_count']}")
    print(f"├─ Predicted sample size: {data_check['pred_sample_count']}")
    print(f"├─ Number of matched samples: {data_check['matched_sample_count']}")
    print(f"├─ Number of missing samples to be predicted: {data_check['missing_in_pred']}")
    print(f"└─ Predicting the number of redundant samples: {data_check['extra_in_pred']}")
    
    overall = eval_result["overall_metrics"]
    print(f"\n[2. Core Evaluation Metrics]")
    print(f"├─ Comprehensive Score (CER50%+F130%+NED20%): {overall['overall_comprehensive_score']:.4f}")
    print(f"├─ CER): {overall['overall_cer']:.4f}")
    print(f"├─ NED: {overall['overall_ned']:.4f}")
    print(f"├─ F1-Score: {overall['overall_f1']:.4f}")
    print(f"├─ Precision: {overall['overall_precision']:.4f}")
    print(f"├─ Recall: {overall['overall_recall']:.4f}")
    print(f"├─ Total Correct Characters: {overall['total_correct_chars']}/{overall['total_ref_chars']}")
    print(f"└─ Editor-in-Chief Distance: {overall['total_edit_distance']}")
    
    errors = eval_result["error_statistics"]
    print(f"\n[3. Error Type Statistics]")
    print(f"├─ Total missing characters (deleted): {errors['total_missing']} ({errors['missing_ratio']:.2%})")
    print(f"├─ Total number of characters (inserted): {errors['total_extra']} ({errors['extra_ratio']:.2%})")
    print(f"└─ Total number of typos (replaced): {errors['total_wrong']} ({errors['wrong_ratio']:.2%})")
    
    print(f"\n[4. Single Sample Details (Top 5)]")
    for i, sample in enumerate(eval_result["sample_details"][:5]):
        print(f"\nSample {i+1}:")
        print(f"├─ Image Path: {sample['image']}")
        print(f"├─ Reference Text: {sample['ref_text']} (length: {sample['ref_length']})")
        print(f"├─ Predictive Text: {sample['pred_text']} (length: {sample['pred_length']})")
        print(f"├─ Core Evaluation Metrics: CER={sample['cer']} | Comprehensive Score={sample['comprehensive_score']}")
        print(f"├─ Supplementary indicators: F1={sample['f1']} | NED={sample['ned']} | precision={sample['precision']} | recall={sample['recall']}")
        print(f"└─ Error Details: Missing character={sample['missing_chars']} | Extra characters={sample['extra_chars']} | Wrong characters={sample['wrong_chars']}")

if __name__ == "__main__":
    REF_JSON_PATH = "/test_data/Dataset_A_true.json"   # Reference Data JSON Path
    PRED_JSON_PATH = "/test_data/Dataset_A_test.json" # Prediction Data JSON Path
    OUTPUT_JSON_PATH = "/eval_A_C_result.json"  # Evaluation Results
    
    try:
        eval_result = evaluate_ocr(REF_JSON_PATH, PRED_JSON_PATH)
        
        # Print Formatted Report
        print_eval_result(eval_result)
        
        # Save results
        with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(eval_result, f, ensure_ascii=False, indent=4)
        print(f"\nThe comprehensive evaluation results have been saved to:{OUTPUT_JSON_PATH}")
    
    except Exception as e:
        print(f"\nEvaluation failed:{str(e)}")