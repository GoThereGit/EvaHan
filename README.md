<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>



# EvaHan 2024

-   EvaHan 2024 is the third International Evaluation of Ancient Chinese Information Processing, focusing this year on the intricate tasks of sentence segmentation and punctuation in ancient Chinese.
-   EvaHan first edition has one task (i.e. a joint task of Sentence Segmentation and Punctuation.
-   EvaHan 2024 is organized by Bin Li, Bolin Chang, Pengxiu Lu, Minxuan Feng, Chao Xu, Liu Liu, Dongbo Wang.



# Important Dates

-   22 December 2023: training data available
-   Evaluation Window
    -   14 February 2024: test data available
    -   24 February 2024: system results due to organizers
-   24 March 2024: reports due to organizers
-   31 March 2024: short report review deadline
-   14 April 2024: camera ready version of reports due to organizers



# Data

The EvaHan 2024 dataset is composed of texts from classical sources, notably *Siku Quanshu* (四库全书), along with other historical texts. The dataset's processing involved initial automatic punctuation and sentence segmentation. Subsequently, these automatic outputs were corrected and refined by experts in Ancient Chinese language to ensure the highest quality of training data and gold standard texts.

The corpus of Chinese ancient classic texts features diachronicity, spanning thousands of years and covering the four traditional types of Chinese canonical texts, namely *Jing* (经), *Shi* (史), *Zi* (子), and *Ji* (集).

## Data Format

All evaluation data are txt files in Unicode (UTF-8) format. The raw texts only contain characters. After manual annotation, punctuation is added to the text, as shown in Table 1.

<p style="text-align:center">Table 1. Example of the Ancient Chinese</p>

|            **Type**             |     **Example**      |
| :-----------------------------: | :------------------: |
|  Raw Text without Punctuation   |   亟請於武公公弗許   |
| Annotated Text with Punctuation | 亟請於武公，公弗許。 |

## Training Data

The training data comprises 10 million characters sourced from the *Siku Quanshu*. The files are presented in UTF-8 plain text using traditional Chinese script.

## Test Data

The test data includes approximately 50,000 characters of Ancient Chinese texts. More details will be provided to the participants before the evaluation.



# Task

This section offers a detailed description of the tasks encompassed in EvaHan 2024.

## Sentence Segmentation and Sentence Punctuation

Sentence segmentation involves converting Chinese text into a sequence of sentences, with each sentence separated by a single space. Additionally, sentence punctuation entails the placement of appropriate punctuation marks at the conclusion of each sentence, as exemplified in Table 2. In numerous Chinese language processing systems, these two processes, sentence segmentation and punctuation, are often addressed together. Consequently, for this shared task, participants are required to automate the transformation of raw text into punctuated text. The evaluation toolkit will assess the effectiveness of both sentence segmentation and punctuation.

<p style="text-align:center">Table 2. Examples of Sentence Segmentation and Sentence Punctuation</p>

|        Raw Text without Punctuation        |   亟請於武公公弗許   |
| :----------------------------------------: | :------------------: |
| Annotated Text with Sentencen Segmentation |  亟請於武公  公弗許  |
|      Annotated Text with Punctuation       | 亟請於武公，公弗許。 |

Please note that EvaHan 2024 does not accept running results with sentence segmentation only.

## Punctuation Set

In the sentence punctuation task, systems are required to assign punctuation to each sentence, as shown in Table 1.

The punctuation set, is shown in Table 3.

<p style="text-align:center">Table 3. Examples of Sentence Segmentation and Sentence Punctuation</p>

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

Each team will initially have access only to the training data. Later, the unlabeled test data will also be released. After the assessment, the labels for the test data will also be released. The scorer employed for EvaHan is a modified version of the one developed for the ref[4]. An illustration of the output of the scorer is given in Table 4. The evaluation will align the system-produced punctuation to the gold standard ones. Then, Sentence Segmentation (SS) and Sentence Punctuation (SP) are evaluated: precision, recall, and F1 score are calculated. The final ranking of teams will be based on the F1 scores. 

<p style="text-align:center">Table 4. Example of scorers' output</p>

|       **Task**        | **Precision** | **Recall** | **F1  Score** |
| :-------------------: | :-----------: | :--------: | :-----------: |
| Sentence Segmentation |     95.00     |   92.00    |     93.48     |
| Sentence Punctuation  |     90.00     |   91.00    |     90.50     |



## Two Modalities

Each participant can submit runs following two modalities. In the closed modality, the resources each team could use are limited. Each team can only use the Training data Text_Train, and the pretrained model XunziALLM. It is word embeddings pretrained on a very large corpus of traditional Chinese collection. Other resources are not allowed in the closed modality.

In the open modality, there is no limit on the resources, data and models. Annotated external data, such as the components or Pinyin of the Chinese characters, word embeddings can be employed. But each team has to state all the resources, data and models they use in each system in the final report. 

Table 5. Pre-trained models for closed modality

| **Model name** |  **Language**   |                       **Description**                        |
| :------------: | :-------------: | :----------------------------------------------------------: |
|   XunziALLM    | Ancient Chinese | Ancient  Chinese RoBERTa pre-trained on  high-quality full-text corpus. |



## Baselines

As a baseline, we will provide the scores obtained on test set using SikuRoBERTa-BiLSTM-CRF (Conditional Random Fields) training on train set without additional resources.



# How to Participate

Participants will be required to submit their runs and to provide a technical report for the task they participated in.

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

Technical reports will be included in the proceedings of the Workshop on Language. Technologies for Historical and Ancient Languages 2024 (LT4HALA 2024) as short papers and published alongside the LREC-COLING proceedings. 

All the reports must:

•    be submitted through the START platform (URL available soon)

•    use the [official LREC-COLING style templates](https://lrec-coling-2024.org/authors-kit/).

•    not exceed four (4) pages of content (excluding references)

•    contain (at least) the following sections: description of the system, results, discussion, and reference.

Reports will receive a light review: we will check for the correctness of the format, the exactness of results and ranking, and overall exposition. If needed, we will contact the authors asking for corrections.



# Participants

-   Researchers who are interested in machine translation and assisted machine translation of Chinese classic texts.
-   Estimated number of participants: 8-20 teams



# Organizers

-   **Dongbo Wang**, College of Information Management, Nanjing Agricultural University, China
-   **Si Shen**, School of Economics and Management, Nanjing University of Science and Technology, China
-   **Minxuan Feng**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Chao Xu**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Lianzhen Zhao**, School of Foreign Languages, China Pharmaceutical University, China
-   **Wenlong Sun**, School of Foreign Languages, Nanjing Tech University, China
-   **Kai Meng**, School of Marxism, Nanjing Agricultural University, China
-   **Bin Li**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Liu Liu**, College of Information Management, Nanjing Agricultural University, China
-   **Wenhao Ye**, College of Information Management, Nanjing Agricultural University, China



# Student Members

-   **Bolin Chang**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Jingxuan Xi**, School of Chinese Language and Literature, Nanjing Normal University, China
-   **Pengxiu Lu**, School of Chinese Language and Literature, Nanjing Normal University, China



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

 
