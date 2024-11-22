<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>



# EvaHan 2025

-   EvaHan 2025 is the fourth International Evaluation of Ancient Chinese Information Processing, focusing on the named entity recognition (NER) tasks of large language models in ancient Chinese.
-   EvaHan 2025 is organized by Dongbo Wang, Bin Li, Yan Zhu, Liu Liu, Shen Si, Chang Liu, Liu Ruilin, Xue Zhao, Bolin Chang, Pengxiu Lu, Minxuan Feng, Chao Xu.



# Important Dates

-   22 December 2024: training data available
-   Evaluation Window
    -   14 February 2025: test data available
    -   24 February 2025: system results due to organizers
-   24 March 2025: reports due to organizers
-   31 March 2025: short report review deadline
-   14 April 2025: camera ready version of reports due to organizers



# Data

The EvaHan 2025 dataset includes 200,000 characters of training data and 2,000 characters of testing data, comprising two types of corpora: historical texts and Traditional Chinese Medicine (TCM) materials. 

Historical texts are carefully selected from *Zuo Zhuan* (左传), *Shi Ji* (史记), and *the Twenty-Four Histories* (二十四史), which together capture thousands of years of Chinese history, encompassing seven types of named entities: person names, geographical locations, book titles, official titles, dynasties, time expressions, etc. 

**The corpus is devoid of punctuation*. 

## Data Format

All evaluation data are txt files in Unicode (UTF-8) format. The raw texts consist solely of characters, and after manual annotation, the texts are presented in a processed format, as shown in Table 1.

<p align="center">Table 1. Example of the Ancient Chinese</p>

|            **Type**             |     **Example**      |
|:--------------------------------|:---------------------|
|  Raw Text (without Punctuation)   |   四年春衞州吁弑桓公而立   |
| Processed Text with Annotations |  四 \t B-T<br>年 \t E-T<br>春 \t O<br>衞 \t B-NS<br>州 \t E-NS<br>吁 \t O<br>弑 \t O<br>桓 \t B-NR<br>公 \t E-NR<br>而 \t O<br>立 \t O   |

## Training Data

The training data comprises 200,000  characters sourced from *Shi Ji* and *the Twenty-Four Histories*. The files are presented in UTF-8 plain text using traditional Chinese script.

## Test Data

The test data includes approximately 2,000 characters of Ancient Chinese texts. More details will be provided to the participants before the evaluation.



# Task

This section offers a detailed description of the tasks encompassed in EvaHan 2025.

## Named Entity Recognition (NER)

In numerous Chinese language processing systems, Named entity recognition (NER) is a critical task often performed alongside other processing functions. NER involves identifying and classifying entities in Chinese text into predefined categories, such as people and locations. The meanings of each annotation label can be found in Table 2 and Table 3.

The evaluation toolkit will assess the effectiveness of the NER process.

<p align="center">Table 2. Examples of Annotation</p>

|   Annotation   |   Meaning  |
| :---: | :---: | 
| NR |  person name   |
| NS |  geographical location  |
| NB |  book title  |
| NO |  official title  |
| NG |  dynasty  |
| T |  time expression  |


<p align="center">Table 3. Examples of NER Annotation using BMEO Tags</p>

|   Annotation   |   Label  |
| :---: | :---: | 
| O |  outside of any named entity  |
| B-NR |  beginning of person name   |
| M-NR |  middle of person name   |
| E-NR |  end of person name   |
| B-NS |  beginning of geographical location  |
| M-NS |  middle of geographical location  |
| E-NS |  end of geographical location  |
| B-NB |  beginning of book title  |
| M-NB |  middle of book title  |
| E-NB |  end of book title  |
| B-NO |  beginning of official title  |
| M-NO |  middle of official title  |
| E-NO |  end of official title  |
| B-NG |  beginning of dynasty  |
| M-NG |  middle of dynasty  |
| E-NG |  end of dynasty  |
| B-T |  beginning of time expression  |
| M-T |  middle of time expression  |
| E-T |  end of time expression  |





## Entity Set

In this task, there are seven categories of entities: person name, geographical location, book title, official title, dynasty and time expression as one track, plus [] as a separate track. These entity types and examples are provided in Table 4. 

<p align="center">Table 4. Examples of Named Entities(Test A: History, 6 categories)</p>

|      **Entity Type**      |   **Example**   |
| :-----------------------: |   :---------:   |
|        person name        |       荆軻      |
|   geographical location   |       長平      |
|        book title         |        易       |
|      official title       |      中大夫      |
|          dynasty          |        秦       | 
|      time expression      |     三十四年     |


<p align="center">Table 4. Examples of Named Entities(Test B: Books 3 categories)</p>



<p align="center">Table 4. Examples of Named Entities(Test C: Traditional Medicine 7 categories)</p>



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
-   **Liu Liu**, College of Information Management, Nanjing Agricultural University, China
-   **Si Shen**, School of Economics and Management, Nanjing University of Science and Technology, China
-   **Dongbo Wang**, College of Information Management, Nanjing Agricultural University, China
-   **Weiguang Qu**, School of Computer and Electronic Information /School of Artificial Intelligence, Nanjing Normal University, China



# Student Members

-   **Bolin Chang**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Jingxuan Xi**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Pengxiu Lu**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Zhixingu Xu**, School of Chinese Language and Literature, Nanjing Normal University, China



# Appendix: Selection of Resources

-   For more information about the EvaHan shared task and the ALP2025 workshop, visit the [official ALP2025 webpage](https://www.ancientnlp.com/alp2025/call_for_papers/).

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

 
