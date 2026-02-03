<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>


[![Zh](https://img.shields.io/badge/README-中文-blue.svg "中文")](./README_zh.md)

**中文版:** <a href="https://github.com/GoThereGit/EvaHan/blob/main/README_zh.md">点此跳转</a> 

## IMPORTANT NEWS
**Registration Entry:** <a href="https://jsj.top/f/nWLK2R">CLICK ME</a>

## EvaHan 2026

-   <a href="https://github.com/GoThereGit/EvaHan"><b>EvaHan 2026</b></a> is the Fifth International Evaluation of Ancient Chinese
    Information Processing, focusing on OCR tasks for multimodal large
    language models in ancient Chinese.

-   Co-organized with LREC 2026, which will be held from May 11 to 16,
    2026, in Mallorca, Spain.

-   Co-organized with LT4HALA 2026, which will be held in Mallorca, Spain.

-   EvaHan 2026 is organized by Dongbo Wang, Bin Li, Minxuan Feng, Chao
    Xu, Weiguang Qu, Liu Liu, Si Shen.

## Previous Tasks

-   EvaHan 2022

The First Bake-off of Ancient Chinese Automatic Processing was
successfully held in Marseille, France, in 2022, with a focus
on automatic word segmentation and part-of-speech tagging of ancient
Chinese.

-   EvaHan 2023

The Second Bake-off of Ancient Chinese Automatic Processing was
successfully held in Macau, China, in 2023, with a focus on machine
translation of ancient Chinese.

-   <a href="https://aclanthology.org/2024.lt4hala-1.27.pdf">EvaHan 2024</a>

The Third Bake-off of Ancient Chinese Automatic Processing was held in
Turin, Italy, in 2024, with a focus on automatic sentence segmentation
and punctuation of ancient Chinese.

-   <a href="https://aclanthology.org/2025.alp-1.19.pdf">EvaHan 2025</a>

The Fourth Bake-off of Ancient Chinese Automatic Processing was held in
New Mexico, USA, in 2025, with a focus on named entity recognition in
ancient Chinese.

## Important Dates for EvaHan 2026(UTC+8 Beijing time)

-   Registration deadline: **January 30, 2026**

-   Training data release: **January 1, 2026**

-   Test data release: **February 3, 2026, 23:50**     ~~**February 1, 2026**~~

-   Running results submission: **February 9, 2026, 23:50** ~~**February 6, 2026**~~

-   Technical report submission deadline: **February 28, 2026**

-   Notification of acceptance: **March 1, 2026**

-   Camera-ready papers due: **March 10, 2026**

## Participation

To participate in EvaHan 2026, you must complete the following steps:

1. <a href="https://jsj.top/f/nWLK2R">**Registration:**</a>\
   Submit a registration form to officially register your team for the
   task. Registration is open from December 1, 2025, to January 30, 2026.
   Only registered participants will gain access to the training dataset.

2. **Accessing the Training Data:**\
   After completing the registration process, participants will receive
   instructions for downloading the training dataset, which includes
   image-text pairs from ancient Chinese texts for OCR.

3. **Submitting Results and Reports:**\
   Participants must use the provided test data to generate results and
   submit their system outputs and a technical report as per the shared
   task schedule.

For inquiries or to request the registration form, please contact us
at [evahan2026@gmail.com](mailto:evahan2025@gmail.com).

## Task
This section offers a detailed description of the tasks encompassed in EvaHan 2026.


Ancient literature, a precious heritage of Chinese civilization, exists primarily in handwritten forms or archaic printed fonts. While diverse in preservation formats, these materials are extremely fragile. Optical Character Recognition (OCR) technology enables the transformation of these paper-based or imaged ancient books into editable digital text, facilitating efficient retrieval, analysis, and dissemination. The application of OCR in this field will significantly enhance the efficiency of literature utilization and promote the digital preservation of cultural heritage. Furthermore, it provides scholars with convenient research tools, fosters the popularization and innovation of knowledge contained in ancient books, and advances the development of the humanities and social sciences.


**Task A: Printed Text Recognition**
Ancient printed fonts present typical challenges such as variant characters, complex layouts, missing characters, and stains, making recognition significantly more difficult than modern printed text. Task A employs Character Error Rate (CER, main metric), F1-score (character/word level), and Normalized Edit Distance (NED) as the evaluation metrics. These metrics comprehensively measure model performance regarding character accuracy, sequence integrity, and edit cost. The task aims to accelerate the digitization of ancient books and improve the practical precision and robustness of automated transcription for printed ancient literature.

**Task B: Layout Element Analysis**
Task B focuses on Layout Element Recognition. The core objective is the precise identification of four key elements within the pages of ancient books: text, image, book_edge, and seal. This task selects mAP (mean Average Precision, main metric), IoU (Intersection over Union), and F1-score as evaluation metrics. These metrics scientifically quantify the model’s recognition effectiveness across multiple dimensions, including detection accuracy, regional matching degree, and comprehensive recognition performance.

**Task C: Handwritten Character Recognition**
The styles of handwritten ancient books are highly personalized and present multiple challenges, including challenges such as cursive connections, variant character forms, stroke omissions, and traces of corrections. Task C adopts Character Error Rate (CER, main metric), F1-score, and Normalized Edit Distance (NED) as evaluation metrics to comprehensively assess model performance in terms of character accuracy, sequence consistency, and edit distance. This task aims to break through technical bottlenecks in the automated transcription of handwritten ancient texts, providing critical support for the digital preservation and in-depth utilization of precious ancient manuscripts.


## Data

The Evahan 2026 dataset comprises three datasets, covering image-text pairs: plain text images, mixed image-text images, and handwritten images-text. The data underwent initial automatic annotation, followed by meticulous correction and refinement by experts in classical Chinese language and history to ensure the highest quality of the training materials and gold-standard texts.

● Dataset A (Printed Texts) consists of data selected from the *Siku Quanshu* (Complete Library of the Four Treasuries), including classics, history, philosophy, and literature, as well as various other ancient books.

● Dataset B (Mixed Layouts) contains mixed image-text data selected from the *Siku Quanshu* and other ancient books.

● Dataset C (Handwritten Texts) includes handwritten ancient books, primarily the Chinese Buddhist canon, including the Chinese Buddhist canon (TKH) dataset, and the Chinese Buddhist canon (MTH) dataset.

**Data Format**

All data is presented in image-text pairs and stored in JSON files with multiple encoding formats. The specific format is shown in Table 1.

Table 1. Examples of Ancient Chinese OCR Corpus

| Picture | Text |
|---------|------|
| <img src="img/image2.png" alt="1761273613524" width="192">  Printed Texts | 欽定四庫全書     史部十一\\n 三呉水考       地理類四{{河渠之屬/}}\\n  提要\\n    {{臣/}}等謹案三呉水考十六卷明張内藴周大\\n    韶仝撰内藴稱呉江生員大韶稱華亭監生\\n    其始末則均未詳也初萬厯四年言官論蘇\\n    松常鎮諸府水利久湮宜及時修濬乞遣御\\n    史一員督其事乃命御史懷安林應訓往應 |
| <img src="img/image3.png" alt="descript" width="233"> Mixed Layouts | {"label": "book_edge", "points": [[2, 14], [17, 14], [17, 655], [2, 655]]}, {"label": "image", "points": [[28, 107], [97, 107], [97, 297], [28, 297]]}, {"label": "image", "points": [[119, 124], [198, 124], [198, 351], [119, 351]]}, {"label": "text", "points": [[219, 60], [254, 60], [254, 171], [219, 171]]}, {"label": "text", "points": [[40, 444], [74, 444], [74, 551], [40, 551]]}, {"label": "text", "points": [[137, 441], [176, 441], [176, 548], [137, 548]]}, {"label": "text", "points": [[276, 23], [321, 23], [321, 137], [276, 137]]}, {"label": "text", "points": [[336, 26], [381, 26], [381, 767], [336, 767]]}, {"label": "image", "points": [[413, 113], [492, 113], [492, 307], [413, 307]]}, {"label": "text", "points": [[430, 442], [472, 442], [472, 518], [430, 518]]} |
| <img src="img/image4.png" alt="" width="293"> Handwritten Texts | 言卽眼識界若有爲若無爲增語是\\n 菩薩摩訶薩卽耳鼻舌身意識界若\\n 有爲若無爲增語是菩薩摩訶薩善\\n 現汝復觀何義言卽眼識界若有漏\\n 若無漏增語非菩薩摩訶薩卽耳鼻\\n 舌身意識界若有漏若無漏增語非\\n 菩薩摩訶薩耶世尊若眼識界有漏\\n 無漏若耳鼻舌身意識界有漏無漏\\n 尚畢竟不可得性非有故況有眼識\\n 界有漏無漏增語及耳鼻舌身意識\\n 界有漏無漏增語此增語旣非有如\\n 何可言卽眼識界若有漏若無漏增\\n 語是菩薩摩訶薩卽耳鼻舌身意識\\n 界若有漏若無漏增語是菩薩摩訶\\n 鼻...... |

**Training Data**
The training set consists of designated portions of subsets A, B, and C. All training samples are provided in image-text pair format, with text in Traditional Chinese, approximately 5000 image-text pairs per subset. Registered participants will receive the training data via email.

**Test Data**
The test set includes the remaining unseen portions of subsets A, B, and C to ensure comprehensive evaluation of all three challenge types. The data is also provided in image-text pair format, approximately 200-500 image-text pairs per subset. Detailed information and a download link for the test data will be provided to participants before the start of the formal evaluation period.


## Metrics

Prior to the official competition commencement, each participating team may only access the training data. Subsequently, the unlabeled test data will be released on February 3, 2026. Following the completion of evaluations, the labels for the test data will also be published. Tables 2 and 3 provide examples of the scorers' outputs. 

Table 2. Character-Level Recognition Performance of the OCR Module

| Task | Precision| Recall | F1_Score | CER  |  NED |
|:---:|:---:|:---:|:---:|:---:|:---:|
| OCR  |  0.75    | 0.98   |  0.34    | 0.41 | 0.32 |

Table 3. Efficacy of the Layout Analysis Module for Page Segmentation

|         Task         |  mAP@[.5:.95]  |   IoU  |Micro-average F1 |Macro-average F1| 
|         :---:        |:---:|:---:|:---:|:---:|
| Page Layout Analysis |      0.88      | 0.79   |     0.56        |     0.71       |


For the three datasets, the evaluation comprises two primary tasks: Task A and C focus on pure text recognition via OCR, assessing metrics such as CER and precision; Task B centers on identifying layout elements in ancient texts, evaluating metrics including mAP and Micro-average F1. Detailed evaluation metrics are presented in Tables 4 and 5.

Table 4. OCR Task Metrics Explanation

<img src="img/image5.png" alt="OCR Task">

Table 5. Page Recognition Task Metrics Specification

<img src="img/image6.png" alt="Page Recognition">

## Evaluation

Before beginning the evaluation, please carefully read the data documentation below!

<a href="https://github.com/GoThereGit/EvaHan/blob/main/EvaHan2026_Dataset_Description.pdf">**Dataset Description!**</a>

1. <a href="https://github.com/GoThereGit/EvaHan/blob/main/task_a_c_eva.py">Evaluation Script</a> for task A and task C.
- The script requires both the reference file and prediction file to be in JSON array format, with each element containing the image_path (as the unique matching identifier) and text fields:

  <img src="img/image9.png" alt="ocr example" width="75%" height="75%">

- **Quick Start**
  - Modify the path: In the `if __name__ == “__main__”:` section of task_a_c_eva.py, modify the following variable: `REF_JSON_PATH` (Reference Data JSON Path); `PRED_JSON_PATH` (Prediction Data JSON Path); `OUTPUT_JSON_PATH` (Evaluation Report Storage Path).
  - Run script: `python task_a_c_eva.py`

2. <a href="https://github.com/GoThereGit/EvaHan/blob/main/task_b_eva.py">Evaluation Script</a> for task B.
- The script requires both reference files and prediction files to be in JSON array format, with each element containing an `image_path` (as the unique matching identifier) and a `regions` field. Within the `regions` field, two mandatory fields—`points` and `label`—must also be included.

  <img src="img/image8.png" alt="example" width="75%" height="75%">
  
- **Quick Start**
  - Modify the path: In the `if __name__ == “__main__”:` section of task_b_eva.py, modify the following variable: `PRED_JSON_PATH`(Prediction Data JSON Path); `GT_JSON_PATH`(Reference Data JSON Path).
  - Run script: `python task_b_eva.py`

## Two Modalities

Each participant can submit results for both Modalities. 

In the closed Modality, each team may only use the official training data, two specified models(Qwen2.5-VL-7B-Instruct or Xunzi_Qwen2_VL_7B_Instruct), or other traditional machine learning models. However, the team should not utilize other corpora as pre-training data or employ other large language models (considering that LLMs are often trained on massive datasets and are unsuitable for closed-domain models).

In the open Modality, there are no restrictions on resources, data, or models. Annotated external data, such as processed images or text, may be used. However, each team must disclose all resources, data, and models used in each system in the final report.

## Baselines

As a baseline, we will provide the scores obtained on test set using
[Qwen/Qwen2.5-VL-7B-Instruct(https://www.modelscope.cn/models/Qwen/Qwen2.5-VL-7B-Instruct)](https://www.modelscope.cn/models/Qwen/Qwen2.5-VL-7B-Instruct) or [Xunzi_Qwen2_VL_7B_Instruct (https://huggingface.co/RAY5/Xunzi_Qwen2_VL_7B_Instruct)](https://huggingface.co/RAY5/Xunzi_Qwen2_VL_7B_Instruct)  training on train set without additional
resources.


## Submitting Running results

Each team can submit up to three runs for two tasks. The closed modality is compulsory, while the open modality is optional.

Once the system has produced the results for the task over the test set, participants have to follow these instructions to complete their submission:

- **Final submission format:**
  - Dataset A, B, and C correspond to training sets A, B, and C respectively. Each participating team must submit three formatted JSON files matching the provided training data format.
  - The naming convention is **TeamID_TestID_runID_modality.json**, such as 14_TestA_1_open.json, meaning that team 11 submits their first run of testA with open modality.
  - Additionally, after organizing all JSON files, the team must bundle them into a single ZIP file for final submission, using the naming format: **TeamID_runID.zip**. For example: 11_3.zip indicates Team 11 submitting their third submission.

- Please submit the annotated test set results via
    [evahan2026@gmail.com](mailto:evahan2025@gmail.com) before February 9, 2026, 23:50 (UTC+8).

- Each team is permitted to submit only three times before the deadline. The final score will be based on the most recent submission.

- Submit your models and codes for validation.(optional)

## Writing the Technical Report 

Technical reports will be peer reviewed. The accepted papers will be included in the proceedings of the **The Fourth Workshop on Language Technologies for Historical and Ancient Languages (LT4HALA 2026)** at **Fifteenth biennial Language Resources and Evaluation Conference (LREC 2026)**, which will take place on May 11，2026, in Mallorca, Spain. 

Submission is electronic, using the Softconf START conference management system via the link: 
https://softconf.com/lrec2026/main

Submissions should be 4 to 5 pages in length (excluding references and Ethics Statements). Submissions should follow the <a href="https://aclanthology.org/2024.lt4hala-1.28.pdf">LREC stylesheet</a>, available on the conference website on the Author’s kit page. All templates are also available from this page. 

At the time of submission, authors are offered the opportunity to share related language resources with the community. All repository entries are linked to the LRE Map, which provides metadata for the resource.  


## Participants

Researchers interested in ancient book OCR based on machine learning and multimodal large models.

## Organizers

-   **Dongbo Wang**, College of Information Management, Nanjing
    Agricultural University, China

-   **Bin Li**, School of Chinese Language and Literature, Nanjing
    Normal University, China

-   **Minxuan Feng**, School of Chinese Language and Literature, Nanjing
    Normal University, China

-   **Chao Xu**, School of Chinese Language and Literature, Nanjing
    Normal University, China

-   **Weiguang Qu**, School of Computer and Electronic Information
    /School of Artificial Intelligence, Nanjing Normal University, China

-   **Liu Liu**, College of Information Management, Nanjing Agricultural
    University, China

-   **Si Shen**, School of Economics and Management, Nanjing University
    of Science and Technology, China

## Student Members

-   **Dongmei Zhu**, College of Information Management, Nanjing
    Agricultural University, China

-   **Jieqiong Li**, College of Information Management, Nanjing
    Agricultural University, China

-  **Ruifeng Wu**,College of Information Management, Nanjing Agricultural
    University, China

-   **Junyi Yang**，College of Information Management, Nanjing Agricultural
    University, China

-   **Zhixing Xu**, School of Chinese Language and Literature, Nanjing
    Normal University, China

-   **Junjie Li**, School of Chinese Language and Literature, Nanjing Normal
    University, China
    
-   **Yue Zhu**, School of Chinese Language and Literature, Nanjing
    Normal University, China
    
-   **Mengting Xu**, School of Chinese Language and Literature, Nanjing normal University, China

## Guiding organizations

-- Ancient Books Intelligent Development and Utilization Committee, China Ancient Books Preservation Association 

## Co-organising organizations

-- Language Intelligence Committee, Chinese Association for Artificial Intelligence

-- Youth Working Committee, Chinese Information Processing Society of China

-- Language Resources and Computational Humanities Committee, The Society of Chinese Minority Languages

-- Natural Language Processing Committee, Jiangsu Provincial Artificial Intelligence Society

-- GULIAN (BEIJING) MEDIA TECH CO.,LTD

## Appendix: Selection of Resources

For more information about the EvaHan shared task and the LREC2026 workshop, visit the [official LREC2026 webpage](https://lrec2026.info/).

OCR Model

-   DeepSeek-OCR: <https://www.modelscope.cn/models/deepseek-ai/DeepSeek-OCR>

-   PaddleOCR-VL:
    <https://www.modelscope.cn/models/PaddlePaddle/PaddleOCR-VL>

-   mscoder/duguang-ocr-onnx-v2:
    https://www.modelscope.cn/models/mscoder/duguang-ocr-onnx-v2

-   RapidAI/RapidOCR: https://www.modelscope.cn/models/RapidAI/RapidOCR

-   iic/cv_convnextTiny_ocr-recognition-document_damo:
    https://www.modelscope.cn/models/iic/cv_convnextTiny_ocr-recognition-document_damo

 
