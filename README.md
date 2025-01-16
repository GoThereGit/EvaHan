<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>

# Notice
-   For teams that successfully registered before **January 15, 2025**, we have sent the training data to the **contact email address** provided in your **agreement document**. Please check your inbox.
-   If any team has not received the training data or has not received a response regarding registration, please contact the EvaHan2025 again at **[evahan2025@gmail.com](mailto:evahan2025@gmail.com)**.

# EvaHan 2025

-   EvaHan 2025 is the fourth International Evaluation of Ancient Chinese Information Processing, focusing on the named entity recognition (NER) tasks of large language models in ancient Chinese.
-   EvaHan2025 will be held at ALP2025 (The Second Workshop on Ancient Languages Processing), co-located with [NAACL2025](https://2025.naacl.org/) (The 2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics).
-   EvaHan 2025 is organized by Bin Li, Bolin Chang, Pengxiu Lu, Minuxan Feng, Chao Xu, Weiguang Qu, Dongbo Wang, Liu Liu, Si Shen, Yan Zhu, Lihong Liu


## Previous Tasks
- EvaHan2022
  - The first bakeoff of ancient Chinese automatic processing, was successfully held in Marseille, France, in 2022, with a focus on **automatic word segmentation and part-of-speech tagging of ancient Chinese**.
- EvaHan2023
  - The second bakeoff of ancient Chinese automatic processing, was successfully held in Macau, China, in 2023, with a focus on **machine translation of ancient Chinese**.
- EvaHan2024
  - The third bakeoff of ancient Chinese automatic processing, was held in Turin, Italy, in 2024, with a focus on **automatic sentence segmentation and punctuation of ancient Chinese**.


## Important Dates for EvaHan 2025

- **Registration deadline**: January 30, 2025  
- **Training data release**: January 15, 2025  
- **Test data release**: February 15, 2025  
- **Running results submission**: February 21, 2025  
- **Technical report submission deadline**: February 28, 2025  
- **Notification of acceptance**: March 5, 2025  
- **Camera-ready papers due**: March 15, 2025  

## Participation

To participate in **EvaHan 2025**, you must complete the following steps:

1. **Registration**:  
   Submit a registration form to officially register your team for the task. Registration is open from **December 1, 2024, to January 15, 2025**. Only registered participants will gain access to the training dataset.  

2. **Accessing the Training Data**:  
   After completing the registration process, participants will receive instructions for downloading the training dataset, which includes 400,000 characters from Ancient Chinese texts annotated for Named Entity Recognition.  

3. **Submitting Results and Reports**:  
   Participants must use the provided test data to generate results and submit their system outputs and a technical report as per the shared task schedule.

For inquiries or to request the registration form, please contact us at **[evahan2025@gmail.com](mailto:evahan2025@gmail.com)**.


# Data
The Evahan 2025 data includes three datasets, encompassing historical and medical texts, with a total of 500,000 characters. The data underwent an initial phase of automatic annotation, followed by meticulous corrections and refinements by experts in Ancient Chinese language and history, ensuring the highest quality of training material and gold-standard texts.

- **Dataset A** is derived from *Shiji* (史记), an ancient Chinese historical masterpiece by Sima Qian, chronicling China's history from mythical times to the Han dynasty, blending biographical and annalistic styles. This dataset contains **6** categories of entities.

- **Dataset B** is derived from *the Twenty-Four Histories* (二十四史), a comprehensive compilation of official Chinese historical records spanning early dynasties through the Ming, documenting governance, culture, and societal evolution. This dataset contains **3** categories of entities.

- **Dataset C** consists of texts on Traditional Chinese Medicine Classics (中医药典籍), covering herbal remedies, acupuncture, and other traditional medical practices. This dataset contains **6** categories of entities.


## Data Format
All evaluation data are txt files in Unicode (UTF-8) format. The raw texts only contain characters and punctuation marks. After manual annotation, the texts are presented in a processed format, as shown in the example files within the [evahan2025_dataset_example](https://github.com/GoThereGit/EvaHan/tree/main/evahan2025/dataset_example) folder.

## Training Data
Training data comprises three datasets, totaling 400,000 characters. The files are presented in UTF-8 plain text using traditional Chinese script. Training data will be sent to your email after registration.

## Test Data
Test data also comprises three datasets, totaling 100,000 characters. More details will be provided to the participants before the evaluation. Download link will be released soon.

# Task

This section offers a detailed description of the tasks encompassed in EvaHan 2025.

## Named Entity Recognition

In numerous Chinese language processing systems, Named entity recognition is a critical task often performed alongside other processing functions. NER involves identifying and classifying entities in Chinese text into predefined categories, such as people and locations. 




## Entity Set

In this task, there are 12 categories of named entities. These entity categories, meanings and examples are provided in Table 1-1, 1-2 and 1-3. 

Table 1-1 Tagset of Named Entities in Dataset A (*Shiji*)

| Annotation |        Meaning        | Example |
|:----------:|:---------------------:|---------|
|     NR     |      person name      | 荆軻      |
|     NS     | geographical location | 長平      |
|     NB     |      book title       | 易       |
|     NO     |    official title     | 中大夫     |
|     NG     |     country name      | 秦       |
|     T      |    time expression    | 三十四年    |



Table 1-2 Tagset of Named Entities in Dataset B (*the Twenty-Four Histories*)

| Annotation |         Meaning          | Example |
|:----------:|:------------------------:|----|
|     NR     |       person name        | 伏羲 |
|     NS     |  geographical location   |  黄河 |
|     T      |     time expression      | 丙戌 |



Table 1-3 Tagset of Named Entities in Dataset C (Traditional Chinese Medicine Classics)

| Annotation |         Meaning          | Example |
|:----------:|:------------------------:|---------|
| ZD  | Traditional  Chinese Medicine disease | 金疮      |
| ZZ  | Syndrome                              | 脾胃虚弱    |
| ZF  | Chinese medicinal  formula            | 当归散     |
| ZP  | decoction pieces                      | 当归      |
| ZS  | symptom                               | 烦满      |
| ZA  | acupoint                              | 承扶      |


# Evaluation

## Metrics

Each team will initially have access only to the training data. Later, the unlabeled test data will also be released. After the assessment, the labels for the test data will also be released. An illustration of the output of the scorer is given in Table 2. The evaluation will align the system-generated named entities with the gold standard. Then, Named Entity Recognition will be evaluated: precision, recall, and F1 score will be calculated. The final ranking of teams will be based on the F1 scores.

Table 2. Example of scorers' output

|       **Task**        | **Precision** | **Recall** | **F1  Score** |
| :-------------------: | :-----------: | :--------: | :-----------: |
|         NER           |     95.00     |   92.00    |     93.48     |




## Two Modalities

Each participant can submit runs following two modalities. In the closed modality, the resources each team could use are limited. Each team can only use the training data, and the pretrained model [GujiRoBERTa_jian_fan](https://huggingface.co/hsc748NLP/GujiRoBERTa_jian_fan). It is word embeddings pretrained on a very large corpus of traditional Chinese collection. Other resources are not allowed in the closed modality.

In the open modality, there is no limit on the resources, data and models. Annotated external data, such as the components or Pinyin of the Chinese characters, word embeddings can be employed. But each team has to state all the resources, data and models they use in each system in the final report. 

<p style="text-align: center">Table 7. Pre-trained models for closed modality</p>

| **Model name** |  **Language**   |                       **Description**                        |
| :------------: | :-------------: | :----------------------------------------------------------: |
|   GujiRoBERTa_jian_fan    | Ancient Chinese | Ancient  Chinese RoBERTa pre-trained on  high-quality full-text corpus. |



## Baselines

As a baseline, we will provide the scores obtained on test set using SikuRoBERTa-BiLSTM-CRF training on train set without additional resources.



# How to Participate

Registration time is mentioned above. Participants will be required to submit their runs and to provide a technical report for the task they participated in.

## Submitting Runs

Each team can submit runs for two tasks. A run should be produced according to the ‘closed modality’. The second run will be produced according to the ‘open modality’. The closed run is compulsory, while the open run is optional.

Once the system has produced the results for the task over the test set, participants have to follow these instructions to complete their submission:

-   Name the runs with the following filename format: `teamID_modality_dataset_submitid.txt` For example: `nnu1_closed_a_1.txt` would be the first run of a team called `nnu1` using the closed modality for the task using `test_a.txt` document. `nnu1_open_b_2.txt` would be the second run of a team called `nnu1` using the open modality for the task using the `test_b.txt` document.
-   Send the file to the following email address: libin.njnu[AT]gmail.com, using the subject "EvaHan Submission: datset - teamName".
-   Each team could submit up to 2 running files for each test file in each modality. Thus, each team could submit up to 8 running files in total.



## Writing the Technical Report

Technical reports will be included in the proceedings of the **Second Workshop on Ancient Language Processing (ALP2025)**, co-located with NAACL 2025, which will take place from April 29 to May 4, 2025, in Albuquerque, New Mexico. The reports will be published as short papers alongside the NAACL proceedings.

All the reports must:

•    be submitted through the START platform (URL will be announced on the [ALP2025 webpage](https://www.ancientnlp.com/alp2025/call_for_papers/))

•    use the [official ACL style templates](https://acl-org.github.io/ACLPUB/formatting.html)

•    not exceed four (4) pages of content (excluding references)

•    include (at least) the following sections: description of the system, results, discussion, and references.

Reports will undergo a light review process to ensure correctness of the format, accuracy of results and rankings, and clarity of exposition. If necessary, authors will be contacted for corrections prior to publication.




# Participants

-   Researchers who are interested in machine translation and assisted machine translation of Chinese classic texts.
-   Estimated number of participants: 8-20 teams



# Organizers

-   **Bin Li**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Minxuan Feng**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Chao Xu**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Weiguang Qu**, School of Computer and Electronic Information /School of Artificial Intelligence, Nanjing Normal University, China
-   **Dongbo Wang**, College of Information Management, Nanjing Agricultural University, China
-   **Liu Liu**, College of Information Management, Nanjing Agricultural University, China
-   **Si Shen**, School of Economics and Management, Nanjing University of Science and Technology, China
-   **Yan Zhu**, Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Science, China
-   **Lihong Liu**, Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Science, China



# Student Members

-   **Bolin Chang**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Ruilin Liu**, College of Information Management, Nanjing Agricultural University, China
-   **Xue Zhao**, College of Information Management, Nanjing Agricultural University, China
-   **Zhixiao Zhao**, College of Information Management, Nanjing Agricultural University, China
-   **Chang Liu**, College of Information Management, Nanjing Agricultural University, China
-   **Yinhao Li**, Liaoning Technology University, China
-   **Bin Li**, Liaoning Technology University, China
-   **Ting Cheng**, Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences, China



# Appendix: Selection of Resources

-   For more information about the EvaHan shared task and the ALP2025 workshop, visit the [official ALP2025 webpage](https://www.ancientnlp.com/alp2025/).

-   Ancient Chinese SikuRoBERTa: https://huggingface.co/SIKU-BERT/sikuroberta;https://github.com/hsc748NLP/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing
-   Modern Chinese RoBERTa: https://huggingface.co/hfl/chinese-roberta-wwm-ext;https://github.com/ymcui/Chinese-BERT-wwm
-   Multilingual version of RoBERTa: https://huggingface.co/xlm-roberta-large;https://github.com/facebookresearch/fairseq/tree/main/examples/xlmr
-   Ancient Chinese GPT-2: https://huggingface.co/uer/gpt2-chinese-ancient;https://github.com/Morizeyao/GPT2-Chinese
-   Ancient Chinese SikuGPT: https://huggingface.co/JeffreyLau/SikuGPT2;https://github.com/SIKU-BERT/sikuGPT
-   GuwenBERT: https://huggingface.co/ethanyt/guwenbert-base;https://github.com/Ethan-yt/guwenbert
-   GujiBERT and GujiGPT: https://github.com/hsc748NLP/GujiBERT-and-GujiGPT
-   Ancient Chinese syntactic corpus: http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/kyodokenkyu/2019-03-08/ 
-   XunziALLM: https://github.com/Xunzi-LLM-of-Chinese-classics/XunziALLM 
-   Ancient Chinese Sentence Segmentation: https://seg.shenshen.wiki/;https://wyd.kvlab.org 
-   Tagged Corpus of Old Chinese: http://lingcorpus.iis.sinica.edu.tw/ancient/ 
-   A very Large Online Ancient Chinese Corpus Retrieval System: http://dh.ersjk.com/ 
-   A GPI Ancient Chinese raw corpus: https://github.com/garychowcmu/daizhigev20 

 
