***
<p style="text-align: center;"><b>LT4HALA 2024</b></p>
<p style="text-align: center;">--<a href="index">Home</a>--&nbsp;&nbsp;--<a href="CFP">CFP</a>--&nbsp;&nbsp;--<a href="EvaLatin">EvaLatin</a>--&nbsp;&nbsp;--EvaHan--&nbsp;&nbsp;--<a href="Program">Program</a>--&nbsp;&nbsp;--<a href="organization">Organization</a>--</p>
***

# EvaHan

![](logo-EvaHan.png)

- [Introduction](#introduction)
- [Important Dates](#important-dates)
- [Data](#data)
  * [Training Data](#training-data)
  * [Test Data](#test-data)
- [Evaluation](#evaluation)
- [How to participate](#how-to-participate)
- [Program](#program)

___



# INTRODUCTION

-   EvaHan 2024 is the third International Evaluation of Ancient Chinese Information Processing, focusing this year on the intricate tasks of sentence segmentation and punctuation in ancient Chinese.
-   EvaHan third edition has one task (i.e. a joint task of Sentence Segmentation and Punctuation.
-   EvaHan 2024 is organized by Bin Li, Bolin Chang, Minxuan Feng, Chao Xu, Liu Liu, Dongbo Wang.



# Important Dates

- 8 January 2024: training data available
- Evaluation Window
  - 1 March 2024: test data available
  - 8 March 2024: system results submission deadline
- 15 March 2024: paper submission deadline
- 24 March 2024: notification of acceptance
- 27 March 2024: camera-ready paper submission
- 20-25 May 2024: workshop

# Data

The EvaHan 2024 dataset is composed of texts from classical sources, notably *Siku Quanshu* (四库全书), along with other historical texts. The dataset's processing involved initial automatic punctuation and sentence segmentation. Subsequently, these automatic outputs were corrected and refined by experts in Ancient Chinese language to ensure the highest quality of training data and gold standard texts.

The corpus of Chinese ancient classic texts features diachronicity, spanning thousands of years and covering the four traditional types of Chinese canonical texts, namely *Jing* (经), *Shi* (史), *Zi* (子), and *Ji* (集).

## Data Format

All evaluation data are txt files in Unicode (UTF-8) format. The raw texts only contain characters. After manual annotation, punctuation is added to the text, as shown in Table 1.

<p align="center">Table 1. Example of the Ancient Chinese</p>

|            **Type**             |     **Example**      |
|:---:|:---:|
|  Raw Text without Punctuation   |   亟請於武公公弗許   |
| Annotated Text with Punctuation | 亟請於武公，公弗許。 |

## Training Data

The training data comprises 10 million characters sourced from the *Siku Quanshu*. The files are presented in UTF-8 plain text using traditional Chinese script. Training data will be sent to your email after registration. 


## Test Data

The test data includes approximately 50,000 characters of Ancient Chinese texts. More details will be provided to the participants before the evaluation. Download link will be released soon.



# Task

This section offers a detailed description of the tasks encompassed in EvaHan 2024.

## Sentence Segmentation and Sentence Punctuation

Sentence segmentation involves converting Chinese text into a sequence of sentences, with each sentence separated by a single space. Additionally, sentence punctuation entails the placement of appropriate punctuation marks at the conclusion of each sentence, as exemplified in Table 2. In numerous Chinese language processing systems, these two processes, sentence segmentation and punctuation, are often addressed together. Consequently, for this shared task, participants are required to automate the transformation of raw text into punctuated text. The evaluation toolkit will assess the effectiveness of both sentence segmentation and punctuation.

<p align="center">Table 2. Examples of Sentence Segmentation and Sentence Punctuation</p>

|        Raw Text without Punctuation        |   亟請於武公公弗許   |
| :----------------------------------------: | :------------------: |
| Annotated Text with Sentencen Segmentation |  亟請於武公    公弗許  |
|      Annotated Text with Punctuation       | 亟請於武公，公弗許。 |

Please note that EvaHan 2024 does not accept running results with sentence segmentation only.

## Punctuation Set

In the sentence punctuation task, systems are required to assign punctuation to each sentence, as shown in Table 1.

The punctuation set, is shown in Table 3.

<p align="center">Table 3. Examples of Sentence Segmentation and Sentence Punctuation</p>

| **Punctuation** |     **Name**     |
| :-------------: | :--------------: |
|       ，        |      Comma       |
|       。        |      Period      |
|       、        |   Slight-pause   |
|       ：        |      Colon       |
|       ；        |    Semicolon     |
|       ？        |     Question     |
|       ！        |   Exclamation    |
|       “”        |  Double Quotes   |
|       ‘’        | Single Quotation |
|      《》       |    Book Title    |



# Evaluation

## Metrics

Each team will initially have access only to the training data. Later, the unlabeled test data will also be released. After the assessment, the labels for the test data will also be released. The scorer employed for EvaHan is a modified version of the one developed for the ref[1]. An illustration of the output of the scorer is given in Table 4. The evaluation will align the system-produced punctuation to the gold standard ones. Then, Sentence Segmentation (SS) and Sentence Punctuation (SP) are evaluated: precision, recall, and F1 score are calculated. The final ranking of teams will be based on the F1 scores. 

<p align="center">Table 4. Example of scorers' output</p>

|       **Task**        | **Precision** | **Recall** | **F1  Score** |
| :-------------------: | :-----------: | :--------: | :-----------: |
| Sentence Segmentation |     95.00     |   92.00    |     93.48     |
| Sentence Punctuation  |     90.00     |   91.00    |     90.50     |



## Two Modalities

Each participant can submit runs following two modalities. In the closed modality, the resources each team could use are limited. Each team can only use the Training data Text_Train, and the pretrained model XunziALLM, which is a large language base model for ancient Chinese processing. Other resources are not allowed in the closed modality.

In the open modality, there is no limit on the resources, data and models. Annotated external data, such as the components or Pinyin of the Chinese characters, word embeddings can be employed. But each team has to state all the resources, data and models they use in each system in the final report. 

<p align="center">Table 5. Pre-trained models for closed modality</p>

| **Model name** |  **Language**   |                       **Description**                        |
| :------------: | :-------------: | :----------------------------------------------------------: |
|   XunziALLM    | Ancient Chinese | Large language base model for ancient Chinese processing. |



## Baselines

As a baseline, we will provide the scores obtained on test set using SikuRoBERTa-BiLSTM-CRF (Conditional Random Fields) training on train set without additional resources.



# How to Participate

Participants will be required to submit their runs and to provide a technical report for the task they participated in.
## Registration
If you are interested in participating, please fill out the electronic application form: [https://forms.office.com/r/jxDBanU7pd](https://forms.office.com/r/jxDBanU7pd). 
When filling it out, please make sure your information is correct and your email address is working. After receiving your registration information, we will send you an email to notify you, please pay attention to check it.


## Submitting Runs

Each team can submit runs for two tasks. A run should be produced according to the ‘closed modality’. The second run will be produced according to the ‘open modality’. The closed run is compulsory, while the open run is optional. 

Once the system has produced the results for the task over the test set, participants have to follow these instructions to complete their submission:

-   Name the runs with the following filename format: 
    testID_teamName_systemID_modality.txt
    For example: *testa_unicatt_1_closed.txt* would be the first run of a team called *unicatt* using the closed modality for the task using *testa.txt* document.
    *testb_unicatt_2_open.txt* would be the second run of a team called *unicatt* using the open modality for the task using the blind testb.txt document.
-    Send the file to the following email address: libin.njnu[AT]gmail.com, using the subject "EvaHan Submission: task - teamName", where the "task" is either *testa* or *testb*.
-   Each team could submit up to 2 running files for each test file in each modality. Thus, each team could submit up to 8 running files in total.

## Writing the Technical Report

Technical reports will be included in the proceedings of the Workshop on Language. Technologies for Historical and Ancient Languages 2024 (LT4HALA 2024) as short papers and published alongside the LREC-COLING proceedings. 

All the reports must:

•    be submitted through the START platform: [START submission page of the workshop](https://softconf.com/lrec-coling2024/lt4hala2024/).

•    use the [official LREC-COLING style templates](https://lrec-coling-2024.org/authors-kit/).

•    not exceed four (4) pages of content (excluding references)

•    contain (at least) the following sections: description of the system, results, discussion, and reference.

Reports will receive a light review: we will check for the correctness of the format, the exactness of results and ranking, and overall exposition. If needed, we will contact the authors asking for corrections.

## Consultation
If you have any questions about this review, please feel free to send an email to our official email: libin.njnu@gmail.com.

# Participants

-   Researchers who are interested in sentence segmentation and punctuation and assisted sentence segmentation and punctuation of Chinese classic texts.
-   Estimated number of participants: 8-20 teams

# Program

| Torino Time | Beijing Time |                   Session                   |
| :---------- | :---------- | :------------------------------------------- |
| 14:00-14:05 | 20:00-20:05 | Opening                                      |
| 14:05-14:15 | 20:05-20:15 | Prof. Zhiwei Feng, *Invited talk*            |
| 14:15-14:35 | 20:15-20:35 | Bin Li, Bolin Chang, Zhixing Xu, Minxuan Feng, Chao Xu, Weiguang Qu, Si Shen, Dongbo Wang, *Overview of EvaHan 2024: the First International Ancient Chinese Sentence Segmentation and Punctuation Evaluation* |
| 14:35-14:43 | 20:35-20:43 | Jie Huang, *Ancient Chinese Punctuation via In-Context Learning* |
| 14:43-14:51 | 20:43-20:51 | Shiquan Wang, Weiwei Fu, Mengxiang Li, Zhongjiang He, Yongxiang Li, Ruiyu Fang, Li Guan, and Shuangyong Song, *Sentence Segmentation and Punctuation for Ancient Books based on Supervised In-context Training* |
| 14:51-14:59 | 20:51-20:59 | Shitu Huo and Wenhui Chen, *Ancient Chinese Sentence Segmentation and Punctuation on Xunzi LLM* |
| 14:59-15:07 | 20:59-21:07 | Xia Tian, Yu Kai, Yu Qianrong and Peng Xinran, *SPEADO: Segmentation and Punctuation for Ancient Chinese Texts via Example Augmentation and Decoding Optimization* |
| 15:07-15:15 | 21:07-21:15 | Xuebin Wang and Zhenghua Li, *Two Sequence Labeling Approaches to Sentence Segmentation and Punctuation Prediction for Classic Chinese Texts* |
| 15:15-15:23 | 21:15-21:23 | Zihong Chen, *Sentence Segmentation and Sentence Punctuation based on XunziALLM* |
| 15:23-15:30 | 21:23-21:30 | Discussion and Closing                        |



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
-   **Zhixing Xu**, School of Chinese Language and Literature, Nanjing Normal University, China



# Appendix: Selection of Resources

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

# Bibliography
[1]	CHENG Ning, LI Bin, XIAO Liming, XU Changwei, GE Sijia, HAO Xingyue, FENG Minxuan. Integration of Automatic Sentence Segmentation and Lexical Analysis of Ancient Chinese based on BiLSTM-CRF Mode.  1st Workshop on Language Technologies for Historical and Ancient Languages, (LT4HALA 2020), pp 52-58. Marseille, 11–16 May 2020.
 

***
<p style="text-align: center;">Back to the <a href="https://circse.github.io/LT4HALA/"><b>Main Page</b></a></p>
***

