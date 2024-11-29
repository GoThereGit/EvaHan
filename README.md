<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>



# EvaHan 2025

-   EvaHan 2025 is the fourth International Evaluation of Ancient Chinese Information Processing, focusing on the named entity recognition (NER) tasks of large language models in ancient Chinese.
-   EvaHan 2025 is organized by Bin Li, Bolin Chang, Pengxiu Lu, Minuxan Feng, Chao Xu, Weiguang Qu, Dongbo Liu, Liu Liu, Si Shen, Yan Zhu, Lihong Liu


## Important Dates for EvaHan 2025

- **Registration for participation/Training data release**: December 1, 2024 - January 15, 2025  
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
   After completing the registration process, participants will receive instructions for downloading the training dataset, which includes 200,000 characters from Ancient Chinese texts annotated for Named Entity Recognition (NER).  

3. **Submitting Results and Reports**:  
   Participants must use the provided test data to generate results and submit their system outputs and a technical report as per the shared task schedule.

For inquiries or to request the registration form, please contact us at **[evahan2025@gmail.com](mailto:evahan2025@gmail.com)**.


# Data
The Evahan 2025 data includes three datasets, encompassing historical and medical texts, with a total of 360 million characters. The data underwent an initial phase of automatic annotation, followed by meticulous corrections and refinements by experts in Ancient Chinese language and history, ensuring the highest quality of training material and gold-standard texts.

- **Dataset A** is derived from *Shiji* (史记), an ancient Chinese historical masterpiece by Sima Qian, chronicling China's history from mythical times to the Han dynasty, blending biographical and annalistic styles. This dataset contains **6** categories of entities.

- **Dataset B** is derived from *the Twenty-Four Histories* (二十四史), a comprehensive compilation of official Chinese historical records spanning early dynasties through the Ming, documenting governance, culture, and societal evolution. This dataset contains **3** categories of entities.

- **Dataset C** consists of texts on Traditional Chinese Medicine Classics (中医药典籍), covering herbal remedies, acupuncture, and other traditional medical practices. This dataset contains **6** categories of entities.


## Data Format
All evaluation data are txt files in Unicode (UTF-8) format. The raw texts only contain characters and punctuation marks. After manual annotation, the texts are presented in a processed format, as shown in the example files within the [evahan2025_dataset_example](https://github.com/GoThereGit/EvaHan/tree/main/evahan2025_dataset_example) folder.

## Training Data
Training data comprises three parts, derived from the three datasets, totaling 300,000 characters. The files are presented in UTF-8 plain text using traditional Chinese script. Training data will be sent to your email after registration.

## Test Data
The test data includes approximately 60,000 characters of Ancient Chinese texts. More details will be provided to the participants before the evaluation. Download link will be released soon.

# Task

This section offers a detailed description of the tasks encompassed in EvaHan 2025.

## Named Entity Recognition (NER)

In numerous Chinese language processing systems, Named entity recognition (NER) is a critical task often performed alongside other processing functions. NER involves identifying and classifying entities in Chinese text into predefined categories, such as people and locations. The meanings of each annotation label can be found in Table 2 and Table 3.

The evaluation toolkit will assess the effectiveness of the NER process.

<p align="center">Table 2. Examples of Annotation</p>

| Annotation |         Meaning          |
|:----------:|:------------------------:| 
|     NR     |       person name        |
|     NS     |  geographical location   |
|     NB     |        book title        |
|     NO     |      official title      |
|     NG     |         dynasty          |
|     NP     |        prescription      |
|     NM     |         medicine         |
|     T      |     time expression      |


<p align="center">Table 3. Examples of NER Annotation using BMEOS Tags</p>

|   Annotation   |  Label  |
| :---: | :---: | 
| O |  outside of any named entity  |
| B-NR |  beginning of person name   |
| M-NR |  middle of person name   |
| E-NR |  end of person name   |
| S-NR |  single person name   |
| B-NS |  beginning of geographical location  |
| M-NS |  middle of geographical location  |
| E-NS |  end of geographical location  |
| S-NS |  single geographical location  |
| B-NB |  beginning of book title  |
| M-NB |  middle of book title  |
| E-NB |  end of book title  |
| S-NB |  single book title  |
| B-NO |  beginning of official title  |
| M-NO |  middle of official title  |
| E-NO |  end of official title  |
| S-NO |  single official title  |
| B-NG |  beginning of dynasty  |
| M-NG |  middle of dynasty  |
| E-NG |  end of dynasty  |
| S-NG |  single dynasty  |
| B-T |  beginning of time expression  |
| M-T |  middle of time expression  |
| E-T |  end of time expression  |
| S-T |  single time expression  |



## Entity Set

In this task, there are seven categories of entities: person name, geographical location, book title, official title, dynasty and time expression as one track, plus [] as a separate track. These entity types and examples are provided in Table 4. 

<p align="center">Table 4. Examples of Named Entities(Dataset A: History, 6 categories)</p>

|      **Entity Type**      |   **Example**   |
| :-----------------------: |   :---------:   |
|        person name        |       荆軻      |
|   geographical location   |       長平      |
|        book title         |        易       |
|      official title       |      中大夫      |
|          dynasty          |        秦       | 
|      time expression      |     三十四年     |


<p align="center">Table 5. Examples of Named Entities(Dataset B: Books 3 categories)</p>



<p align="center">Table 6. Examples of Named Entities(Dataset C: Traditional Medicine 6 categories)</p>



# Evaluation

## Metrics

Each team will initially have access only to the training data. Later, the unlabeled test data will also be released. After the assessment, the labels for the test data will also be released. The scorer employed for EvaHan is a modified version of the one developed for the ref[4]. An illustration of the output of the scorer is given in Table 5. The evaluation will align the system-generated named entities with the gold standard. Then, Named Entity Recognition (NER) will be evaluated: precision, recall, and F1 score will be calculated. The final ranking of teams will be based on the F1 scores.

<p align="center">Table 5. Example of scorers' output</p>

|       **Task**        | **Precision** | **Recall** | **F1  Score** |
| :-------------------: | :-----------: | :--------: | :-----------: |
|         NER           |     95.00     |   92.00    |     93.48     |




## Two Modalities

Each participant can submit runs following two modalities. In the closed modality, the resources each team could use are limited. Each team can only use the Training data Text_Train, and the pretrained model XunziALLM. It is word embeddings pretrained on a very large corpus of traditional Chinese collection. Other resources are not allowed in the closed modality.

In the open modality, there is no limit on the resources, data and models. Annotated external data, such as the components or Pinyin of the Chinese characters, word embeddings can be employed. But each team has to state all the resources, data and models they use in each system in the final report. 

<p align="center">Table 6. Pre-trained models for closed modality</p>

| **Model name** |  **Language**   |                       **Description**                        |
| :------------: | :-------------: | :----------------------------------------------------------: |
|   XunziALLM    | Ancient Chinese | Ancient  Chinese RoBERTa pre-trained on  high-quality full-text corpus. |



## Baselines

As a baseline, we will provide the scores obtained on test set using SikuRoBERTa-BiLSTM-CRF (Conditional Random Fields) training on train set without additional resources.



# How to Participate

Registration time is mentioned above. Participants will be required to submit their runs and to provide a technical report for the task they participated in.

## Submitting Runs

Each team can submit runs for two tasks. A run should be produced according to the ‘closed modality’. The second run will be produced according to the ‘open modality’. The closed run is compulsory, while the open run is optional. 

Once the system has produced the results for the task over the test set, participants have to follow these instructions to complete their submission:

-   Name the runs with the following filename format: 
    testID_teamName_systemID_modality.txt
    For example: *testa_unicatt_1_closed.txt* would be the first run of a team called *unicatt* using the closed modality for the task using *testa.txt* document.
    *testb_unicatt_2_open.txt* would be the second run of a team called *unicatt* using the open modality for the task using the blind testb.txt document.
-    Send the file to the following email address: libin.njnu[AT]gmail.com, using the subject “EvaHan Submission: task - teamName”, where the “task” is either *testa* or *testb*.
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
-   **Yan Zhu**, Institute of Information on Traditional Chinese Medicine, China
-   **Lihong Liu**, Institute of Information on Traditional Chinese Medicine, China



# Student Members

-   **Bolin Chang**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Ruilin Liu**, College of Information Management, Nanjing Agricultural University, China
-   **Xue Zhao**, College of Information Management, Nanjing Agricultural University, China



# Appendix: Selection of Resources

-   For more information about the EvaHan shared task and the ALP2025 workshop, visit the [official ALP2025 webpage](https://www.ancientnlp.com/alp2025/).

-   Ancient Chinese SikuRoBERTa: https://huggingface.co/SIKU-BERT/sikuroberta;https://github.com/hsc748NLP/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing
-   Modern Chinese RoBERTa: https://huggingface.co/hfl/chinese-roberta-wwm-ext;https://github.com/ymcui/Chinese-BERT-wwm
-   Multilingual version of RoBERTa: https://huggingface.co/xlm-roberta-large;https://github.com/facebookresearch/fairseq/tree/main/examples/xlmr
-   Ancient Chinese GPT-2: https://huggingface.co/uer/gpt2-chinese-ancient;https://github.com/Morizeyao/GPT2-Chinese
-   Ancient Chinese SikuGPT: https://huggingface.co/JeffreyLau/SikuGPT2;https://github.com/SIKU-BERT/sikuGPT
-   GuwenBERT: https://huggingface.co/ethanyt/guwenbert-base;https://github.com/Ethan-yt/guwenbert
-   Ancient Chinese syntactic corpus: http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/kyodokenkyu/2019-03-08/ 
-   XunziALLM: https://github.com/Xunzi-LLM-of-Chinese-classics/XunziALLM 
-   Ancient Chinese Sentence Segmentation: https://seg.shenshen.wiki/;https://wyd.kvlab.org 
-   Tagged Corpus of Old Chinese: http://lingcorpus.iis.sinica.edu.tw/ancient/ 
-   A very Large Online Ancient Chinese Corpus Retrieval System: http://dh.ersjk.com/ 
-   A GPI Ancient Chinese raw corpus: https://github.com/garychowcmu/daizhigev20 

 
