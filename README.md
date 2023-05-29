<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>

# EvaHan2023

* Evaluation of Natural Language Processing (NLP) tools for the Ancient Chinese language
* Machine Translation from Ancient Chinese to Modern Chinese/English
* Co-operated with [ALT2023](https://github.com/GoThereGit/ALT)， Macau SAR, China on Sep 4, 2023, [MT-SUMMIT2023](https://mtsummit2023.scimeeting.cn/en/web/index/)
* Past Events: <a href='https://circse.github.io/LT4HALA/2022/EvaHan'>Evahan2022</a>

# Important Dates

* Registration for the shared task: 15 Feb, 2023 ~ 25 May, 2023
* Training data release: April 1, 2023
* Test data release: June 7, 2023
* Data submission : June 14, 2023
* Tech report submission: June 22, 2023
* Notification of acceptance: June 31, 2023
* Camera Ready submission: 15 July 2023

# Data

Training data for evaluation is excerpted from the Twenty-Four Histories(dynastic histories from remote antiquity till the Ming Dynasty), the Pre-Qin classics and “ZiZhi TongJian (资治通鉴, Comprehensive Mirror in Aid of Governance)”,which was finished by the research group of the National Social Science Foundation of China major project “Research on the Construction and Application of Cross-language Knowledge Base of Ancient Chinese Classics” (project No. :21&ZD331) . Among them, the Twenty-Four Histories is the general name of the twenty-four official histories written by various dynasties in ancient China; the Pre-Qin  classics are the historical materials of the Pre-Qin period(Paleolithic Period ~ 221 B.C.), which have an important position in ancient books, including history books and sub-books; “ZiZhi TongJian” is a chronological history book compiled by historians of the Northern Song Dynasty, covering sixteen dynasties from 403 B.C. to 959 A.D. over a span of 1362 years.
The Chinese ancient classic texts in the corpus feature both diachronicity(i.e. spanning thousands of years)(i.e. covering the four traditional types of Chinese canonical texts). The four are _Jing_ (经), *shi* (史), *zi* (子) and *ji* (集).

## Data Format

All evaluation data are txt files in Unicode (UTF-8) format , arranged by two fields of source language and  target language to form a sentence level parallel corpus,as shown in Table 1 and Table 2.
<p align="center">Table 1. Example of the  Ancient Chinese to Modern Chinese corpus</p>

|Ancient-Chinese|Modern-Chinese|
|:---:|:---:|
|后妃表|后妃表|
|后妃之制，厥有等威，其来尚矣。|后妃的制度，有它的等级威儀，它的由來很久遠。|
|元初，因其國俗，不娶庶姓，非此族也，不居嫡選。|元朝初年，因襲蒙古的習俗，不娶異姓，不是后族的，不處在可以選爲正妻的地位。|
|當時使臣為舅甥之貴，蓋有周姬、齊姜之遺意，歷世守之，因可嘉也。|當時的史臣以爲皇族后族的尊貴，原有周姬、齊姜的遺意，歷代都遵守它，本來是可以表彰的。|

Table 1 shows an example of the Ancient Chinese to Modern Chinese parallel corpus. On the left side is the Ancient Chinese text, and on the right side is the Modern Chinese (traditional Chinese) text corresponding to the sentence unit.

<p align="center">Table 2. Example of the  Ancient Chinese to English corpus</p>

|Ancient-Chinese|English|
|:---:|:---:|
|杜密素與李膺名行相次，|Du Mi had shared in reputation with Li Ying,|
|起，對之揖，勸令從學。|He stood up and bowed to him, then urged him to study.|
|濟陰黃允，以俊才知名。|Huang Yun of Jiyin was known for his outstanding talents.|
|兵士喜悅，大小皆出。|Officers and men were delighted, and they all went out to take part.|
|獵者來還，莫不潤涕。|When the men came back from the hunt, every one of them wept for sorrow.|
|榮恐不免，詣闕自論。|Kou Rong was afraid he would not escape [this combination of hostility] and he [sought to] go back to the palace to plead his case.|

Table 2 shows an example of the Ancient Chinese to English parallel corpus. On the left side is the Ancient Chinese text, and on the right side is the English text corresponding to the sentence unit.

## Training Data

The source of the training data includes the Ancient-Chinese-to-Modern-Chinese parallel texts of China Twenty-four Histories, the Ancient-Chinese-to-English parallel texts of Pre-Qin classcis and “Zizhi Tongjian”. 

Descriptions about the overall parallel texts for machine translation are presented in Table 3.

<p align="center">Table 3. Detail of training data in EvaHan 2023</p>

| Data Source | Source Data |Target Data|
|:---:|:---:|:---:|
| Ancient-Chinese-to-Modern-Chinese parallel texts of China Twenty-four Histories | 9,583,749 characters for the original Chinese Classic texts | 12,763,534 characters |
| Ancient-Chinese-to-English parallel texts of Pre-Qin canonical texts and Zizhi Tongjian | 618,083 characters for the original Ancient Chinese texts | 838,321 words |

Briefly, the training data employed in this task embodies many new features, such as the large-scale and well-balanced data as well as its comprehensiveness from the diachronic perspective.

## Test Data

The test data only provides Ancient Chinese texts(the source language),and one test data set is provided for Ancient Chinese to Modern Chinese machine translation  and Ancient Chinese to English machine translation , about 2000 sentences each.

More details will be provided to the participants after the evaluation.

# Task

The cross-lingual machine translation of Chinese classic texts consists of two parts: **the Ancient-Chinese-to-Modern-Chinese machine translation** and **the Ancient-Chinese-to-English machine translation**.

## Task Objective

The goals of the translation task are:
*	To investigate the applicability of current MT techniques in ancient Chinese translation.
*	To examine the significant challenges in ancient Chinese translation (e.g. word order and syntax problems).
*	Provide a platform for the enthusiasts of machine translation in ancient Chinese
* To further machine translation research for ancient Chinese and the exploration of  forefront machine translation technology.


## Task Requirements

The difference between Ancient Chinese-Modern Chinese translation task and Ancient Chinese-English translation task is that the source corpus is different and the model specified in the closed mode is different. 

You can choose either or both of them to participate in, with the same metrics for evaluation is employed. Although the Chinese data in the training corpus is all traditional, you can also choose to submit simplified translation results when submitting the Ancient Chinese-Modern Chinese translation results, and the test data in the evaluation includes both versions.

Although the main goal of this evaluation is to identify the best performing machine translation project, we encourage creative projects to enter the competition even if their performance is not optimal. Participants can also use this evaluation to further improve their project.

# Evaluation

## Metrics

We will evaluate the performance of the Ancient-Chinese-to-English machine translation model and Ancient-Chinese-to-Modern-Chinese machine translation model provided by the participants. The scorers employed for EvaHan 2023 are based on **BLEU (Bilingual Evaluation Understudy)**,**chrF** and **COMET-QE**.

Each participating team will initially have access only to the training data. Later, test data containing only ancient Chinese texts will also be released. After the assessment, the modern Chinese or English texts corresponding to the ancient Chinese in the test data will also be released.

The BLEU metrics measures machine translation quality by word-level n-grams. It is a modified version of the sacreBLEU , which provides hassle-free computation of shareable, comparable, and reproducible BLEU scores. The ChrF metrics evaluates the character-level translation quality and adds a recall metric, thus improving the correlation with human judgment. The COMET-QE is a state-of-the-art metric based on pre-trained models designed to predict human language experts’ judgments of machine translation quality, often with the highest accuracy.

## Two Modalities

Each participant can submit runs following two modalities. In the closed modality, the resources each team could use are limited. Each team can only use the Training data (Training data name, TBD), and the following pre-trained models listed in Table 3. Other resources are not allowed in the closed modality.
<p align="center">Table 3. Pre-trained models for closed modality</p>

|Pre-Trained Model|Language|Description|
|:---:|:---:|:---:|
|Siku-RoBERTa|Ancient Chinese|Ancient Chinese RoBERTa pre-trained  on high-quality “Siku Quanshu (四库全书)” full-text corpus.|
|Chinese-RoBERTa-wwm-ext|Modern Chinese|Modern Chinese pre-trained RoBERTa with Whole Word Masking strategy.|
|RoBERTa|English|Pre-trained model on English with MLM objective.|

In the open modality, however, there is no limit on the resources, data and models. Annotated external data, such as the components, Pinyin of the Chinese characters, word embeddings, dictionaries, KGs, etc. can be employed. But each team has to state all the resources, data and models they use in each system in the final report.
<p align="center">Table 4. Limitations on the two modalities.</p>

|Limits|Closed Modality|Open Modality|
|---|---|---|
|Machine learning algorithm|No limit|No limit|
|Pre-trained model|Only models mentioned in Table 3|No limit|
|Training data|Only (Training data name, TBD)|No limit|
|Features used|Only from (Training data name, TBD)|No limit|
|Manual correction|Not allowed|Not allowed|

## Baselines

We will evaluate the translated outputs of Google Translate on the test data and use the scores as the baseline.

# How to Praticipate

## Registration

If you would like to participate in this shared task, please fill out the [registration form](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAMAAExHmLlUMURNSUNHQTQ5SUhQMzFIR05GSEo2QUFONi4u&lang=en) and ensure that your information is correct and your email is able to receive messages. Once we receive your registration information, we will send the training data to your email address. Please check your email regularly.

If you have any questions about this shared task, please feel free to send an email to our official email address: evahan2023@gmail.com.

If you do not receive a reply for a long time, please check if your email was sent successfully.

## Submitting Runs

Once the system has produced the results for the task over the test set, participants have to follow these instructions for completing your submission:

### File naming

Name the runs with the following filename format:

taskID_teamName_systemID_modality.tsv

For example: testa_unicatt_1_closed.tsv would be the first run of a team called unicatt using the closed modality for the task using testa.txt(TBD) document (the Ancient-Chinese-to-Modern-Chinese machine translation).

testb_unicatt_2_open.tsv would be the second run of a team called unicatt using the open modality for the task using testb.txt(TBD) document (the Ancient-Chinese-to-English machine translation).

### Submission format

The output files for system-level rankings should be formatted as a tab-separated values (TSV) in the following way:

**\<id>\\t\<source>\\t\<translation>[\\t\<translation>]**

Each field should be delimited by a single tab character.

Where:

**\<id>** is the ID of source data (original ancient Chinese text).

**\<source>** is the original ancient Chinese text.

**< translation >** is the machine translation result of your system, the second machine translation result is optional.

<p align="center">Table 5. Example of submission format</p>
  
| id | source | translation |
|:---:|:---:|:---:|
| 1	| 植，琰之兄女婿也。 |	Cao Zhi had married a daughter of Cui Yan's elder brother. |
| 2 | 眾嘉嚴畯能以實讓。 |	All admired the honest way that Yan Jun had refused the appointment. |
| 3 | 操曰：“凡人也。” |	A common fellow, replied Cao Cao. |
| 4 | 然則何為自往？ |	Then why go yourself? |
### How to submit
  
Before you submit, please run your scores files through a validation script, which we will provide later. You can use it along with either BLEU, chrF or COMET-QE sys.

Submissions should be sent to evahan2023@gmail.com with the subject “EvaHan Submission: taskID - teamName”, where the “taskID” is either testa(TBD) or testb(TBD).

You can make up to 2 submissions per language pair, per team.

## Writing the Technical Report
Papers should not be longer than 4 pages for content (for references, unlimited number of pages is allowed). The papers must follow the MT Summit 2023 style guides (PDF version, LaTeX version, MS Word version, and [Overleaf template](https://www.overleaf.com/latex/templates/mt-summit-2023-template/knrrcnxhkqxd) and be submitted in PDF format. To allow for blind reviewing, please do not include author names and affiliations within the paper and avoid obvious self-references.

Papers must be submitted to the [website](https://softconf.com/mtsummit2023/research) by the conference submission deadline.

# Participants
  
* Researchers who are interested in machine translation and assisted machine translation of Chinese classic texts.
* Estimated number of participants: 8-20 teams

# Organizers
  
* **Dongbo Wang**, College of Information Management, Nanjing Agricultural University, China
* **Si Shen**, School of Economics and Management, Nanjing University of Science and Technology, China
* **Minxuan Feng**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Chao Xu**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Lianzhen Zhao**, School of Foreign Languages, China Pharmaceutical University, China
* **Wenlong Sun**, School of Foreign Languages, Nanjing Tech University, China
* **Bin Li**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Liu Liu**, College of Information Management, Nanjing Agricultural University, China
* **Wenhao Ye**, College of Information Management, Nanjing Agricultural University, China

# Student Members
  
* **Bolin Chang**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Chun Yu**, College of Information Management, Nanjing Agricultural University, China
* **Dayu Yan**, School of Economics & Management, Nanjing University of Science and Technology, China
* **Chang Liu**, College of Information Management, Nanjing Agricultural University, China
* **Die Hu**, College of Information Management, Nanjing Agricultural University, China
* **Feng Xie**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Hai Zhang**, College of Information Management, Nanjing Agricultural University, China
* **Haotian Hu**, School of Information Management, Nanjing University, China
* **Huan Liu**, College of Information Management, Nanjing Agricultural University, China
* **Kaixin Yin**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Li Yang**, College of Information Management, Nanjing Agricultural University, China
* **Litao Lin**, College of Information Management, Nanjing Agricultural University, China
* **Na Wu**, College of Information Management, Nanjing Agricultural University, China
* **Yizhou Yin**, School of Economics & Management, Nanjing University of Science and Technology, China
* **Yuan Liang**, College of Information Management, Nanjing Agricultural University, China
* **Yue Qi**, College of Information Management, Nanjing Agricultural University, China
* **Zhixiao Zhao**, College of Information Management, Nanjing Agricultural University, China
* **Zhixing Xu**, School of Chinese Language and Literature, Nanjing Normal University, China

# Guidelines
  
* [EvaHan2023_Guidelines](./EvaHan2023_Guidelines.pdf)

# Appendix: Selection of Resources
*	[Ancient Chinese SikuRoBERTa(model)](https://huggingface.co/SIKU-BERT/sikuroberta); [Ancient Chinese SikuRoBERTa(description)](https://github.com/hsc748NLP/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing)
*	[Modern Chinese RoBERTa(model)](https://huggingface.co/hfl/chinese-roberta-wwm-ext); [Modern Chinese RoBERTa(description)](https://github.com/ymcui/Chinese-BERT-wwm)
*	[English RoBERTa(model)](https://huggingface.co/roberta-large); [English RoBERTa(description)](https://github.com/facebookresearch/fairseq/tree/main/examples/roberta)
*	[Multilingual version of RoBERTa(model)](https://huggingface.co/xlm-roberta-large); [Multilingual version of RoBERTa(description)](https://github.com/facebookresearch/fairseq/tree/main/examples/xlmr)
*	[Ancient Chinese GPT-2(model)](https://huggingface.co/uer/gpt2-chinese-ancient); [Ancient Chinese GPT-2(description)](https://github.com/Morizeyao/GPT2-Chinese)
*	[Ancient Chinese SikuGPT(model)](https://huggingface.co/JeffreyLau/SikuGPT2); [Ancient Chinese SikuGPT(description)](https://github.com/SIKU-BERT/sikuGPT)
*	[GuwenBERT(model)](https://huggingface.co/ethanyt/guwenbert-base); [GuwenBERT(description)](https://github.com/Ethan-yt/guwenbert)
*	[Ancient Chinese syntactic corpus](http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/kyodokenkyu/2019-03-08/)
*	[Ancient Chinese Sentence Segmentation](https://seg.shenshen.wiki) 
*	[Tagged Corpus of Old Chinese](http://lingcorpus.iis.sinica.edu.tw/ancient/) 
*	[A very Large Online Ancient Chinese Corpus Retrieval System](http://dh.ersjk.com/) 
*	[A GPI Ancient Chinese raw corpus](https://github.com/garychowcmu/daizhigev20)

