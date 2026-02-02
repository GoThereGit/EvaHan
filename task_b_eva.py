"""
=============================================================================
Layout Detection Evaluation Script
=============================================================================

This script evaluates layout detection performance by computing:
- mAP@[.5:.95]: Mean Average Precision across IoU thresholds from 0.5 to 0.95
- Micro F1: F1 score calculated from aggregated TP, FP, FN across all labels
- Macro F1: Average of F1 scores for each individual label
- Average Match IoU: Mean IoU of all matched bounding boxes

Data Format:
    The input JSON files should contain an array of samples with:
    {
        "image_path": "path/to/image.png",
        "regions": [
            {
                "label": "text|table|figure|title|...",
                "text": "OCR content (optional, not used for evaluation)",
                "points": [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
            }
        ]
    }

Note: This evaluator only considers bounding box positions and label types.
      OCR text content is not evaluated.

Author: Evaluation Script
License: MIT
=============================================================================
"""

import json
import os
import sys
import numpy as np
from collections import defaultdict
from typing import List, Tuple, Dict


class ProgressBar:
    """
    A simple console progress bar for tracking long-running operations.

    Attributes:
        total (int): Total number of items to process
        current (int): Current number of items processed
        desc (str): Description text to display before the progress bar
        bar_width (int): Width of the progress bar in characters
    """

    def __init__(self, total: int, desc: str = "Processing"):
        """
        Initialize the progress bar.

        Args:
            total: Total number of items to process
            desc: Description text to display before the progress bar
        """
        self.total = total
        self.current = 0
        self.desc = desc
        self.bar_width = 50

    def update(self, n: int = 1) -> None:
        """
        Update the progress bar by incrementing the current count.

        Args:
            n: Number of items to increment by (default: 1)
        """
        self.current += n
        percent = self.current / self.total
        filled = int(self.bar_width * percent)
        bar = '=' * filled + '-' * (self.bar_width - filled)
        sys.stdout.write(f'\r{self.desc}: [{bar}] {self.current}/{self.total} ({percent*100:.1f}%)')
        sys.stdout.flush()
        if self.current >= self.total:
            print()

    def close(self) -> None:
        """Close the progress bar by printing a newline if not complete."""
        if self.current < self.total:
            print()


class BBox:
    """
    Bounding Box class representing a layout region.

    The BBox is defined by 4 corner points and calculates the minimum
    enclosing axis-aligned rectangle for IoU computation.

    Attributes:
        points (List[List[int]]): Original 4 corner points [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
        label (str): Label type (e.g., 'text', 'table', 'figure', 'title')
        rect (Tuple[int, int, int, int]): Minimum enclosing rectangle as (x_min, y_min, x_max, y_max)
        area (int): Area of the minimum enclosing rectangle in pixels squared
    """

    def __init__(self, points: List[List[int]], label: str):
        """
        Initialize a BBox from 4 corner points.

        Args:
            points: List of 4 corner points [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
            label: Label type for this bounding box
        """
        self.points = points
        self.label = label

        # Calculate minimum enclosing rectangle (axis-aligned bounding box)
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        self.rect = (min(xs), min(ys), max(xs), max(ys))

        # Calculate area of the enclosing rectangle
        self.area = (self.rect[2] - self.rect[0]) * (self.rect[3] - self.rect[1])

    def iou(self, other: 'BBox') -> float:
        """
        Calculate Intersection over Union (IoU) with another bounding box.

        IoU is computed using the minimum enclosing rectangles of both boxes.
        Formula: IoU = Area_of_Intersection / Area_of_Union

        Args:
            other: Another BBox object to compute IoU with

        Returns:
            IoU value between 0.0 and 1.0, where 1.0 indicates perfect overlap
        """
        # Find intersection rectangle coordinates
        x1 = max(self.rect[0], other.rect[0])
        y1 = max(self.rect[1], other.rect[1])
        x2 = min(self.rect[2], other.rect[2])
        y2 = min(self.rect[3], other.rect[3])

        # Calculate intersection area (0 if no overlap)
        inter = max(0, x2 - x1) * max(0, y2 - y1)

        # Calculate union area
        union = self.area + other.area - inter

        # Return IoU, avoiding division by zero
        return inter / union if union > 0 else 0.0


class LayoutEvaluator:
    """
    Layout Detection Evaluator for computing detection metrics.

    This evaluator computes standard object detection metrics for layout analysis:
    - mAP@[.5:.95]: Mean Average Precision at IoU thresholds 0.5, 0.55, ..., 0.95
    - Micro/Macro F1 scores
    - Average IoU of matched boxes

    Attributes:
        iou_threshold (float): IoU threshold for considering a prediction as correct
        match_ious (List[float]): List of IoU values for all matched boxes (populated during evaluation)
    """

    def __init__(self, iou_threshold: float = 0.5):
        """
        Initialize the LayoutEvaluator.

        Args:
            iou_threshold: Minimum IoU for a prediction to be considered a true positive (default: 0.5)
        """
        self.iou_threshold = iou_threshold

    def load_data(self, json_path: str) -> Dict[str, List[Tuple[BBox, str]]]:
        """
        Load layout detection data from a JSON file.

        The JSON file should contain an array of samples, each with:
        - image_path: Path to the image file
        - regions: Array of detected regions with label and points

        Args:
            json_path: Path to the JSON file to load

        Returns:
            Dictionary mapping filename to list of (bbox, label) tuples
            Format: {filename: [(BBox, label), ...]}
        """
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        result = defaultdict(list)

        for sample in data:
            # Extract filename from image path (handle both \\ and / separators)
            image_path = sample["image_path"]
            filename = image_path.replace("\\", "/").split("/")[-1]

            # Process each region in the sample
            for region in sample.get("regions", []):
                points = region["points"]
                label = region["label"]

                # Only process regions with exactly 4 corner points
                if len(points) == 4:
                    bbox = BBox(points, label)
                    result[filename].append((bbox, label))

        return dict(result)

    def match_single_image(self, pred_boxes: List[Tuple[BBox, str]],
                           gt_boxes: List[Tuple[BBox, str]]) -> Dict:
        """
        Match predicted boxes with ground truth boxes for a single image.

        This method performs per-label matching using a greedy algorithm:
        1. Group boxes by label type
        2. Build an IoU matrix for each label
        3. Greedily match boxes with highest IoU above the threshold

        Args:
            pred_boxes: List of (BBox, label) tuples for predictions
            gt_boxes: List of (BBox, label) tuples for ground truth

        Returns:
            Dictionary mapping label to its TP/FP/FN statistics
            Format: {label: {"tp": int, "fp": int, "fn": int}}
        """
        # Group boxes by label
        pred_by_label = defaultdict(list)
        gt_by_label = defaultdict(list)

        for bbox, label in pred_boxes:
            pred_by_label[label].append(bbox)
        for bbox, label in gt_boxes:
            gt_by_label[label].append(bbox)

        # Initialize statistics for each label
        stats = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})

        # Perform matching for each label present in ground truth
        for label, gt_list in gt_by_label.items():
            pred_list = pred_by_label.get(label, [])

            # Build IoU matrix (rows: predictions, columns: ground truth)
            iou_matrix = np.zeros((len(pred_list), len(gt_list)))
            for i, p in enumerate(pred_list):
                for j, g in enumerate(gt_list):
                    iou_matrix[i, j] = p.iou(g)

            # Greedy matching: match predictions to ground truth with highest IoU
            matched_pred = set()
            matched_gt = set()

            # Sort predictions by their maximum IoU with any ground truth box
            for i in np.argsort(-iou_matrix.max(axis=1) if len(pred_list) > 0 else []):
                if i in matched_pred:
                    continue

                max_iou = iou_matrix[i].max()

                # Skip if IoU is below threshold
                if max_iou < self.iou_threshold:
                    continue

                # Find the best matching ground truth box
                j = np.argmax(iou_matrix[i])

                # Skip if this ground truth is already matched
                if j in matched_gt:
                    continue

                # Record a true positive
                stats[label]["tp"] += 1
                matched_pred.add(i)
                matched_gt.add(j)

                # Store the IoU for this match (for average IoU calculation)
                self.match_ious.append(max_iou)

            # Count false positives (unmatched predictions)
            stats[label]["fp"] = len(pred_list) - len(matched_pred)

            # Count false negatives (unmatched ground truth)
            stats[label]["fn"] = len(gt_list) - len(matched_gt)

        # Handle labels that appear in predictions but not in ground truth (all false positives)
        for label in pred_by_label:
            if label not in gt_by_label:
                stats[label]["fp"] = len(pred_by_label[label])

        return stats

    def calculate_ap(self, pred_boxes: List[BBox], gt_boxes: List[BBox],
                     iou_th: float) -> float:
        """
        Calculate Average Precision (AP) for a single label at a specific IoU threshold.

        Since predictions don't have confidence scores, we use IoU with ground truth
        as a proxy for ranking. This is a simplified AP calculation.

        The AP is computed using 11-point interpolation on the Precision-Recall curve.

        Args:
            pred_boxes: List of predicted BBox objects
            gt_boxes: List of ground truth BBox objects
            iou_th: IoU threshold for considering a prediction as correct

        Returns:
            Average Precision value between 0.0 and 1.0
        """
        # Edge case: no predictions or no ground truth
        if len(gt_boxes) == 0 or len(pred_boxes) == 0:
            return 0.0

        # Calculate maximum IoU of each prediction with any ground truth box
        pred_scores = []
        for p in pred_boxes:
            max_iou = max(p.iou(g) for g in gt_boxes)
            pred_scores.append((p, max_iou))

        # Sort predictions by IoU in descending order (as a proxy for confidence)
        pred_scores.sort(key=lambda x: -x[1])

        # Build Precision-Recall curve
        tp_cumsum = 0
        fp_cumsum = 0
        precision_list = []
        recall_list = []

        gt_matched = [False] * len(gt_boxes)
        total_gt = len(gt_boxes)

        for pred_box, max_iou in pred_scores:
            # Find the best matching ground truth box for this prediction
            best_idx = -1
            best_iou = 0
            for idx, gt_box in enumerate(gt_boxes):
                if gt_matched[idx]:
                    continue
                iou_val = pred_box.iou(gt_box)
                if iou_val > best_iou:
                    best_iou = iou_val
                    best_idx = idx

            # Count as true positive if IoU exceeds threshold
            if best_idx != -1 and best_iou >= iou_th:
                tp_cumsum += 1
                gt_matched[best_idx] = True
            else:
                fp_cumsum += 1

            # Calculate precision and recall at this point
            precision = tp_cumsum / (tp_cumsum + fp_cumsum) if (tp_cumsum + fp_cumsum) > 0 else 0
            recall = tp_cumsum / total_gt
            precision_list.append(precision)
            recall_list.append(recall)

        # Calculate AP using 11-point interpolation
        if len(precision_list) == 0:
            return 0.0

        ap = 0.0
        for t in np.linspace(0, 1, 11):
            # Find maximum precision at recall level >= t
            p_interp = [p for r, p in zip(recall_list, precision_list) if r >= t]
            ap += max(p_interp) if p_interp else 0
        ap /= 11

        return ap

    def evaluate(self, pred_json: str, gt_json: str) -> Dict:
        """
        Execute the full evaluation pipeline.

        This method:
        1. Loads prediction and ground truth data from JSON files
        2. Matches predictions to ground truth for each image
        3. Calculates mAP@[.5:.95], micro/macro F1, and average IoU
        4. Prints detailed results and returns metrics

        Args:
            pred_json: Path to the predictions JSON file
            gt_json: Path to the ground truth JSON file

        Returns:
            Dictionary containing all evaluation metrics:
            {
                "mAP@[.5:.95]": float,
                "micro_f1": float,
                "macro_f1": float,
                "avg_match_iou": float,
                "micro_precision": float,
                "micro_recall": float,
                "label_stats": Dict[str, Dict]  # Per-label statistics
            }
        """
        print("Loading data...")
        pred_data = self.load_data(pred_json)
        gt_data = self.load_data(gt_json)

        print(f"Number of predicted images: {len(pred_data)}")
        print(f"Number of ground truth images: {len(gt_data)}")

        # Find common images between predictions and ground truth
        common_images = set(pred_data.keys()) & set(gt_data.keys())
        print(f"Number of common images: {len(common_images)}")

        # Reset match IoU storage for this evaluation
        self.match_ious = []

        # Aggregate statistics across all images
        label_stats = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})

        # Collect all boxes by label (for mAP calculation across all images)
        pred_boxes_by_label = defaultdict(list)
        gt_boxes_by_label = defaultdict(list)

        # Process each image
        pbar = ProgressBar(len(common_images), desc="Matching images")
        for filename in common_images:
            pred_boxes = pred_data[filename]
            gt_boxes = gt_data[filename]

            # Store boxes grouped by label
            for bbox, label in pred_boxes:
                pred_boxes_by_label[label].append(bbox)
            for bbox, label in gt_boxes:
                gt_boxes_by_label[label].append(bbox)

            # Perform matching for this image
            stats = self.match_single_image(pred_boxes, gt_boxes)
            for label, stat in stats.items():
                label_stats[label]["tp"] += stat["tp"]
                label_stats[label]["fp"] += stat["fp"]
                label_stats[label]["fn"] += stat["fn"]

            pbar.update()

        # Print IoU distribution diagnostics
        print(f"\n[IoU Distribution Diagnostics]")
        print(f"Number of successful matches: {len(self.match_ious)}")
        if self.match_ious:
            print(f"Maximum IoU: {max(self.match_ious):.4f}")
            print(f"Minimum IoU: {min(self.match_ious):.4f}")
            print(f"Average IoU: {np.mean(self.match_ious):.4f}")
            print(f"Count with IoU >= 0.5: {sum(1 for i in self.match_ious if i >= 0.5)}")
            print(f"Count with IoU >= 0.3: {sum(1 for i in self.match_ious if i >= 0.3)}")
            print(f"Count with IoU < 0.3: {sum(1 for i in self.match_ious if i < 0.3)}")
        else:
            print("WARNING: No boxes were matched!")

        # Calculate mAP@[.5:.95]
        iou_thresholds = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
        ap_by_threshold = []

        print("\nCalculating mAP...")
        pbar_map = ProgressBar(len(iou_thresholds), desc="IoU thresholds")

        for iou_th in iou_thresholds:
            aps = []
            # Calculate AP for each label at this IoU threshold
            for label in set(pred_boxes_by_label.keys()) | set(gt_boxes_by_label.keys()):
                ap = self.calculate_ap(pred_boxes_by_label[label], gt_boxes_by_label[label], iou_th)
                aps.append(ap)
            ap_by_threshold.append(np.mean(aps) if aps else 0)
            pbar_map.update()

        # mAP is the mean of AP values across all IoU thresholds
        map_value = np.mean(ap_by_threshold)

        # Calculate micro-averaged F1 score
        total_tp = sum(s["tp"] for s in label_stats.values())
        total_fp = sum(s["fp"] for s in label_stats.values())
        total_fn = sum(s["fn"] for s in label_stats.values())

        micro_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
        micro_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
        micro_f1 = 2 * micro_precision * micro_recall / (micro_precision + micro_recall) if (micro_precision + micro_recall) > 0 else 0

        # Calculate macro-averaged F1 score (average of per-label F1 scores)
        f1_scores = []
        for label, stat in label_stats.items():
            tp, fp, fn = stat["tp"], stat["fp"], stat["fn"]
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
            f1_scores.append(f1)

        macro_f1 = np.mean(f1_scores) if f1_scores else 0

        # Calculate average IoU of all matched boxes
        avg_match_iou = np.mean(self.match_ious) if self.match_ious else 0

        # Print final results
        print("\n" + "=" * 60)
        print("EVALUATION RESULTS")
        print("=" * 60)
        print(f"mAP@[.5:.95]:  {map_value:.4f}")
        print(f"Micro F1:       {micro_f1:.4f} (P={micro_precision:.4f}, R={micro_recall:.4f})")
        print(f"Macro F1:       {macro_f1:.4f}")
        print(f"Avg Match IoU:  {avg_match_iou:.4f}")
        print("=" * 60)

        # Print detailed statistics for each label
        print("\nPer-Label Statistics:")
        print(f"{'Label':<15} {'TP':>6} {'FP':>6} {'FN':>6} {'Prec':>6} {'Rec':>6} {'F1':>6}")
        print("-" * 60)
        for label in sorted(label_stats.keys()):
            stat = label_stats[label]
            tp, fp, fn = stat["tp"], stat["fp"], stat["fn"]
            prec = tp / (tp + fp) if (tp + fp) > 0 else 0
            rec = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
            print(f"{label:<15} {tp:>6} {fp:>6} {fn:>6} {prec:>6.3f} {rec:>6.3f} {f1:>6.3f}")

        return {
            "mAP@[.5:.95]": map_value,
            "micro_f1": micro_f1,
            "macro_f1": macro_f1,
            "avg_match_iou": avg_match_iou,
            "micro_precision": micro_precision,
            "micro_recall": micro_recall,
            "label_stats": dict(label_stats)
        }


if __name__ == "__main__":
    """
    Example usage of the LayoutEvaluator.

    Modify the paths below to point to your prediction and ground truth JSON files.
    """
    # Configure file paths
    PRED_JSON = r"path\to\your\predictions.json"
    GT_JSON = r"path\to\your\ground_truth.json"

    # Create evaluator with default IoU threshold of 0.5
    evaluator = LayoutEvaluator(iou_threshold=0.5)

    # Run evaluation
    results = evaluator.evaluate(PRED_JSON, GT_JSON)
