<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>



# EvaHan 2025

-   EvaHan 2025 is the fourth International Evaluation of Ancient Chinese Information Processing, focusing on the named entity recognition (NER) tasks of large language models in ancient Chinese.
-   EvaHan 2025 is organized by Dongbo Wang, Bin Li, Yan Zhu, Liu Liu, Shen Si, Chang Liu, Liu Ruilin, Xue Zhao, Bolin Chang, Pengxiu Lu, Minxuan Feng, Chao Xu.


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

The EvaHan 2025 dataset includes 300,000 characters of training data and 60,000 characters of testing data, comprising two types of corpora: historical texts and Traditional Chinese Medicine (TCM) materials. 

Historical texts are carefully selected from *Shi Ji* (史记) and *the Twenty-Four Histories* (二十四史), which together capture thousands of years of Chinese history, encompassing seven types of named entities: person names, geographical locations, book titles, official titles, dynasties, time expressions, etc. 

Traditional Chinese Medicine (TCM) materials are


## Data Format

All data are txt files in Unicode (UTF-8) format. After manual annotation, the texts are presented in a processed format, as shown in Table 1.

<p align="center">Table 1. Example of the Ancient Chinese</p>

|            **Type**             |     **Example**      |
|:--------------------------------|:---------------------|
|  Raw Text  |   四年春衞州吁弑桓公而立   |
| Processed Text with Annotations |  四 \t B-T<br>年 \t E-T<br>春 \t O<br>衞 \t B-NS<br>州 \t E-NS<br>吁 \t O<br>弑 \t O<br>桓 \t B-NR<br>公 \t E-NR<br>而 \t O<br>立 \t O   |

### Training Data

#### *Shiji*

Records of the Grand Historian (*Shiji*) is a biographical historical text compiled by Sima Qian. It chronicles history from the legendary Yellow Emperor to the reign of Emperor Wu. The work consists of 130 volumes, including 12 volumes of annals (benji), 30 volumes of hereditary houses (shijia), 70 volumes of ranked biographies (liezhuan), 10 volumes of tables (biao), and 8 volumes of treatises (shu).The Shiji corpus is divided into a training set and a test set.

The training set contains 162,680 Chinese characters in total, comprising 11,138 sentences. Files are presented in UTF-8 plain text using traditional Chinese script.

##### Example

The training data of *Shiji* is provided in a character-level format. 

- **Each line contains one Chinese character, followed by a tab (`\t`), and then the corresponding label.**
- **Sentences are separated by a blank line.** 

Below is an example of the training data format. 

秦	S-NG<br>聞	O<br>公	B-NR<br>子	E-NR<br>死	O<br>，	O<br>使	O<br>蒙	B-NR<br>驁	E-NR<br>攻	O<br>魏	S-NG<br>，	O<br>拔	O<br>二	O<br>十	O<br>城	O<br>，	O<br>初	O<br>置	O<br>東	B-NS<br>郡	E-NS<br>。	O<br><br>其	O<br>後	O<br>秦	S-NG<br>稍	O<br>蠶	O<br>食	O<br>魏	S-NG<br>，	O<br>十	O<br>八	O<br>歲	O<br>而	O<br>虜	O<br>魏	O<br>王	O<br>，	O<br>屠	O<br>大	B-NS<br>梁	E-NS<br>。	O<br><br>高	B-NR<br>祖	E-NR<br>始	O<br>微	O<br>少	O<br>時	O<br>，	O<br>數	O<br>聞	O<br>公	B-NR<br>子	E-NR<br>賢	O<br>。	O<br>

Below is a table illustrating the comparison between raw text and annotated training data. The left column shows the **raw text**, and the right column shows the corresponding **annotated training data**.

In the raw text, sentences are segmented based on punctuation marks: **“。”**, **“？”**, and **“！”**. Additionally, in the specific context of *Shi Ji* (史记), quotation marks **“「”**, **“」”**, **“『”**, and **“』”** are also considered as sentence delimiters.

<p align="center">Table . Raw Text vs. Annotated Training Data (Shiji)</p>

| **Raw Text** (原始语料)                          | **Annotated Training Data** (训练语料)                   |
|--------------------------------------------------|---------------------------------------------------------|
| 秦聞公子死，使蒙驁攻魏，拔二十城，初置東郡。  | 秦	S-NG<br>聞	O<br>公	B-NR<br>子	E-NR<br>死	O<br>，	O<br>使	O<br>蒙	B-NR<br>驁	E-NR<br>攻	O<br>魏	S-NG<br>，	O<br>拔	O<br>二	O<br>十	O<br>城	O<br>，	O<br>初	O<br>置	O<br>東	B-NS<br>郡	E-NS<br>。	O<br> |
| 其後秦稍蠶食魏，十八歲而虜魏王，屠大梁。        | 其	O<br>後	O<br>秦	S-NG<br>稍	O<br>蠶	O<br>食	O<br>魏	S-NG<br>，	O<br>十	O<br>八	O<br>歲	O<br>而	O<br>虜	O<br>魏	O<br>王	O<br>，	O<br>屠	O<br>大	B-NS<br>梁	E-NS<br>。	O<br> |
| 高祖始微少時，數聞公子賢。                    | 高	B-NR<br>祖	E-NR<br>始	O<br>微	O<br>少	O<br>時	O<br>，	O<br>數	O<br>聞	O<br>公	B-NR<br>子	E-NR<br>賢	O<br>。	O<br> |


#### *The Twenty-Four Histories*

The Twenty-Four Histories is the collective term for the official dynastic histories of China, written in a biographical style. These works provide a comprehensive overview of ancient Chinese society, including politics, economy, military affairs, culture, astronomy, and geography. The corpus consists of a training set and a test set. 

The training set contains 209,798 Chinese characters in 7,783 sentences. Files are presented in UTF-8 plain text using traditional Chinese script.

##### Example

The training data of *The Twenty-Four Histories* is provided in a character-level format. Similar to the corpus of *Shiji*, the comparison between the raw text and the annotated data is as follows:

<p align="center">Table . Raw Text vs. Annotated Training Data (The Twenty-Four Histories)</p>

| **Raw Text** (原始语料)                          | **Annotated Training Data** (训练语料)                   |
|--------------------------------------------------|---------------------------------------------------------|
| 開禧三年，史彌遠自詹事入樞府，乃進兼賓客。     | 開	B-T<br>禧	E-T<br>三	B-T<br>年	E-T<br>，	O<br>史	B-NR<br>彌	M-NR<br>遠	E-NR<br>自	O<br>詹	O<br>事	O<br>入	O<br>樞	O<br>府	O<br>，	O<br>乃	O<br>進	O<br>兼	O<br>賓	O<br>客	O<br>。	O<br> |
| 貫俱聽命，各視力所致，争以侈麗高廣相夸尚，而延福宫、景龍江之役起，浸淫及於艮嶽矣。 | 貫	S-NR<br>俱	O<br>聽	O<br>命	O<br>，	O<br>各	O<br>視	O<br>力	O<br>所	O<br>致	O<br>，	O<br>争	O<br>以	O<br>侈	O<br>麗	O<br>高	O<br>廣	O<br>相	O<br>夸	O<br>尚	O<br>，	O<br>而	O<br>延	B-NS<br>福	M-NS<br>宫	E-NS<br>、	O<br>景	B-NS<br>龍	M-NS<br>江	E-NS<br>之	O<br>役	O<br>起	O<br>，	O<br>浸	O<br>淫	O<br>及	O<br>於	O<br>艮	B-NS<br>嶽	E-NS<br>矣	O<br>。	O<br> |
| 三年，有司奏減河北、河東并淮南礬額，計十六萬緡。 | 三	B-T<br>年	E-T<br>，	O<br>有	O<br>司	O<br>奏	O<br>減	O<br>河	B-NS<br>北	E-NS<br>、	O<br>河	B-NS<br>東	E-NS<br>并	O<br>淮	B-NS<br>南	E-NS<br>礬	O<br>額	O<br>，	O<br>計	O<br>十	O<br>六	O<br>萬	O<br>緡	O<br>。	O<br> |
| 張洎，滁州全椒人。曾祖旼，澄城尉。祖蘊，泗上轉運巡官。父煦，滁州司法掾。 | 張	B-NR<br>洎	E-NR<br>，	O<br>滁	B-NS<br>州	E-NS<br>全	B-NS<br>椒	E-NS<br>人	O<br>。	O<br>曾	O<br>祖	O<br>旼	S-NR<br>，	O<br>澄	B-NS<br>城	E-NS<br>尉	O<br>。	O<br>祖	O<br>蘊	S-NR<br>，	O<br>泗	B-NS<br>上	E-NS<br>轉	O<br>運	O<br>巡	O<br>官	O<br>。	O<br>父	O<br>煦	S-NR<br>，	O<br>滁	B-NS<br>州	E-NS<br>司	O<br>法	O<br>掾	O<br>。	O<br> |





## Test Data

The test data includes approximately 60,000 characters of Ancient Chinese texts. More details will be provided to the participants before the evaluation.

#### *Shiji*

The test set consists of 40,495 Chinese characters, comprising 3,192 sentences. 

#### *The Twenty-Four Histories*

The test set comprises 23,165 Chinese characters in 865 sentences.


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

 
