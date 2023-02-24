<div align='center'>
<img src = 'https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png'>
</div>

# EvaHan2023
* Evaluation of Natural Language Processing (NLP) tools for the Ancient Chinese language
* Machine Translation from Ancient Chinese to Mandarin Chinese/English
* Co-operated with ALT2023
* Past Events: <a href='https://circse.github.io/LT4HALA/2022/EvaHan'>Evahan2022</a>

# Important Dates
* CFP in Dec.2022 (depends on ALT's schedule)
* Reg for the shared task: Juan 1, 2023 ~ March 1, 2023
* Training data release: April 1, 2023
* Test data release: TBD
* Data submission : TBD
* Tech report submission: TBD

# Task
The cross-lingual machine translation of Chinese classic texts consists of two parts: **the Ancient-Chinese-to-Modern-Chinese machine translation** and **the Ancient-Chinese-to-English machine translation**. Chinese ancient classics are the important part of traditional Chinese culture. In the field of ancient literature research, the translation of classical Chinese texts plays a very important role. Classical Chinese differs greatly from modern Chinese in grammar, syntax, vocabulary, and other aspects. Improving the machine translation performance from Classical Chinese to Modern Chinese can better promote the study of ancient literature. Improving the machine translation technology from Classical Chinese to English can also accelerate the promotion of Chinese traditional culture worldwide.

## Task Objective
The goals of the translation task are:
* To investigate the applicability of current MT techniques when translating classical Chinese into English or modern Chinese
* To examine special challenges in translating between classical Chinese and English or modern Chinese, including word order and syntax
* To create publicly available corpora for machine translation and evaluation of classical Chinese
* To provide practical experience of the most advanced machine translation methods for beginners in the field of machine translation
* To prompt the development of machine translation research for classical Chinese and advance the forefront of machine translation technology exploration

## Task Requirements
We will provide parallel corpora of Classical Chinese-Modern Chinese based on the Twenty-Four Histories and Classical Chinese-English based on pre-Qin texts, respectively, as training and testing data for Classical Chinese-Modern Chinese and Classical Chinese-English machine translation. We will also provide several unified models, using Chinese-RoBERTa-wwm-ext for Modern Chinese , Siku-RoBERTa for Classical Chinese and RoBERTa for English. The goal is to improve the model and enhance machine translation performance.

You can choose to participate in one or both of the tasks, and we will use the same metrics for evaluation. For each task, we provide subtasks of two tracks, i.e., closed track and open track. To ensure the fairness of the competition, in the closed track, please use the data we provide as the training data only. However, you can use other models and resources to build the translation system in open track, or just build your own model. If additional data is used, participants should clearly indicate which data is from the provided dataset and which is from external sources. This will allow us to evaluate the performance of the models on our provided dataset separately from their performance on external data.

Each participant should include a brief introduction of their translation system when submitting, including basic information such as the models (if any), techniques, methods used, etc. Each participant should submit a technical reports emphasizing improvements made to the model, techniques used, and methods applied.
While the main purpose of this evaluation is to select the most superior machine translation system, if you think your approach is very interesting, even if its performance is not very superior, you are welcome to participate in the evaluation, and you can further improve your system through this evaluation.

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
* **Die Hu**, College of Information Management, Nanjing Agricultural University, China
* **Feng Xie**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Hai Zhang**, College of Information Management, Nanjing Agricultural University, China
* **Haotian Hu**, School of Information Management, Nanjing University, China
* **Huan Liu**, College of Information Management, Nanjing Agricultural University, China
* **Kaixin Yin**, School of Chinese Language and Literature, Nanjing Normal University, China
* **Li Yang**, College of Information Management, Nanjing Agricultural University, China
* **Litao Lin**, College of Information Management, Nanjing Agricultural University, China
* **Na Wu**, College of Information Management, Nanjing Agricultural University, China
* **Yuan Liang**, College of Information Management, Nanjing Agricultural University, China
* **Yue Qi**, College of Information Management, Nanjing Agricultural University, China
* **Zhixiao Zhao**, College of Information Management, Nanjing Agricultural University, China
* **Zhixing Xu**, School of Chinese Language and Literature, Nanjing Normal University, China

# Data
The data comes from China Twenty-four Histories , Pre-Qin canonical texts and “ZiZhi TongJian (资治通鉴, Comprehensive Mirror in Aid of Governance)”. The PDF text is converted into word format through OCR recognition, and the team members manually proofread the corpus by using the convenient platform for chapter, paragraph, and sentence alignment , and finally get the parallel corpus. Among them, China Twenty-four Histories is the general name of the twenty-four official histories written by various dynasties in ancient China, all of which are compiled in the biography style; the Pre-Qin canonical texts are the historical materials of the pre-Qin period, which have an important position in ancient books, including history books and sub-books; “ZiZhi TongJian” is a chronological history book compiled by historians of the Northern Song Dynasty, covering 1362 years of history of sixteen dynasties.

The Chinese classic texts in the corpus feature both diachronicity, i.e. spanning thousands of years, as well as diversity, i.e. covering the four traditional types of Chinese canonical texts: Jing (经, Confucian classics), shi (史, historical works), zi (子, philosophical works belonging to schools of thought other than the Confucian but also including works on agriculture, medicine, mathematics, astronomy, divination, art criticism, and other miscellaneous writings) and ji (集, collection of literary works).

Both English and modern Chinese translations are selected for these texts in the parallel corpus. The specific parallel texts provided for this test are as follows.
The cross-lingual machine translation of Chinese classic texts consists of two parts: 
## Data Format
The released data is not tokenized and includes sentences of any length (including empty sentences). All data is in Unicode (UTF-8) format. The Table1. below gives an example of the parallel corpus data format:
<p align="center">Table 1. Data format of the aligned sentences</p>

|Classical-Chinese|Modern-Chinese|
|:---:|:---:|
|后妃表|后妃表|
|后妃之制，厥有等威，其来尚矣。|后妃的制度，有它的等级威儀，它的由來很久遠。|
|元初，因其國俗，不娶庶姓，非此族也，不居嫡選。|元朝初年，因襲蒙古的習俗，不娶異姓，不是后族的，不處在可以選爲正妻的地位。|
|當時使臣為舅甥之貴，蓋有周姬、齊姜之遺意，歷世守之，因可嘉也。|當時的史臣以爲皇族后族的尊貴，原有周姬、齊姜的遺意，歷代都遵守它，本來是可以表彰的。|

On the left side is the ancient Chinese text, and on the right side is the modern Chinese text corresponding to the sentence-based unit. For the ancient Chinese-English parallel texts, the same format is followed.
## Train Data
The source of the training data is the parallel corpus of Classical-Chinese-to-Modern-Chinese parallel texts of China Twenty-four Histories and Classical-Chinese-to-English parallel texts of Pre-Qin canonical texts and “Zizhi Tongjian”. 

The overall parallel texts for machine translation are presented as follows.
<p align="center">Table 2. Detail of training data in EvaHan 2023</p>

| Data Source | Selecting criteria | Total data |
|:---:|:---:|:---:|
| Classical-Chinese-to-Modern-Chinese parallel texts of China Twenty-four Histories | Sentences of Chinese classic texts of seven characters or more in length | 322,473 sentence pairs in total; 9,583,749 characters for the original Chinese Classic texts and 12,763,534 characters for the Modern Chinese translations |
| Classical-Chinese-to-English parallel texts of Pre-Qin canonical texts and Zizhi Tongjian (资治通鉴, “Comprehensive Mirror in Aid of Governance”) | Sentences of Chinese classic texts of seven characters or more in length and the corresponding English translations | 22,277 sentence pairs in total, including 618,083 characters in the original Classical Chinese texts and 838,321 words in the English translations |

In this task, the cross-lingual parallel corpus of Chinese classic texts is large-scale, diachronic, and well-balanced.

## Test Data
Overview and usage of the test data. （TBD待定）

# Evaluation
## Metrics
We will evaluate the performance of the Ancient-Chinese-to-English machine translation model and Ancient-Chinese-to-Modern-Chinese machine translation model provided by the participants. The scorers employed for EvaHan 2023 are based on BLEU[4] (Bilingual Evaluation Understudy) and TER (Translation Error Rate).

Each participating team will initially have access only to the training data. Later, test data containing only ancient Chinese texts will also be released. After the assessment, the modern Chinese or English texts corresponding to the ancient Chinese in the test data will also be released.

The BLEU metrics is a modified version of the sacreBLEU, which provides hassle-free computation of shareable, comparable, and reproducible BLEU scores. The TER metrics is commonly used to determine the amount of post-editing required for machine translation outputs. The evaluation will automatically calculate the scores based on the generated outputs and the corresponding reference translations. The final ranking will be based on BLEU score.

## Two Modalities
Each participant can submit runs following two modalities. In the closed modality, the resources each team could use are limited. Each team can only use the Training data (Training data name, TBD待定), and the following pre-trained models listed in Table 3. Other resources are not allowed in the closed modality.
<p align="center">Table 3. Pre-trained models for closed modality</p>

|Pre-Trained Model|Language|Description|
|:---:|:---:|:---:|
|Siku-RoBERTa|Ancient Chinese|Ancient Chinese RoBERTa pre-trained  on high-quality “Siku Quanshu (四库全书)” full-text corpus.|
|Chinese-RoBERTa-wwm-ext|Modern Chinese|Modern Chinese pre-trained RoBERTa with Whole Word Masking strategy.|
|RoBERTa|English|Pre-trained model on English with MLM objective.|

In the open modality, however, there is no limit on the resources, data and models. Annotated external data, such as the components, Pinyin of the Chinese characters, word embeddings, dictionaries, KGs, etc. can be employed. But each team has to state all the resources, data and models they use in each system in the final report.
<p align="center">Table 4. Limitations on the two modalities.</p>
  <div style="text-align:center">
  
|Limits|Closed Modality|Open Modality|
|:---:|:---:|:---:|
|Machine learning algorithm|No limit|No limit|
|Pre-trained model|Only models mentioned in Table 4|No limit|
|Training data|Only (Training data name, TBD待定)|No limit|
|Features used|Only from (Training data name, TBD待定)|No limit|
|Manual correction|Not allowed|Not allowed|
  
  </div>
## Baselines
* TBD
# Guidelines
* TBD
