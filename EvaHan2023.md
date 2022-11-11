![image](https://user-images.githubusercontent.com/54113513/201254029-e63dd695-22aa-4419-ac01-7fc34326625a.png)
# EvaHan2023
Evaluation of Natural Language Processing (NLP) tools for the Ancient Chinese language

# Task
Chinese classic texts have played a vital role in shaping the unique character and sense of national identity of the Chinese people. They “represent an integral part of world civilization and a treasure that should be shared by all peoples of the world” (Wang Rongpei). Introducing effectively the thoughts, culture, knowledge and wisdom contained in Chinese classic texts to the world is an important way to deepen the world’s understanding of China and to achieve better cultural exchange between China and the world. With the rapid advancement of foreign cultural exchanges, there has arisen an intense demand for knowledge of Chinese classic texts in the international community. Nevertheless, the existing cross-lingual corpora of Chinese classic texts have a relatively small amount of data because they usually include a particular canonical text, thus lacking systematicity and diachronicity. Consequently, there are relatively inadequate researches on cross-lingual machine translation of Chinese classic texts. Against such backdrop, utilizing the platform which can facilitate the alignment of chapters, paragraphs and sentences, we obtained the distribution characteristics of the cross-lingual Chinese classic texts in terms of parallel chapters, paragraphs and sentences by analyzing the selected cross-lingual Chinese classic texts. We also achieved the automatic alignment of chapters, paragraphs and sentences for the cross-lingual Chinese classic texts based on the corresponding rules, statistics as well as traditional machine learning and deep learning strategies. As an ancient written language, the Classical Chinese with its conciseness differs from English and modern Chinese in respect to vocabulary, word order and syntax. Hence, certain background knowledge is required to understand Classical Chinese accurately. On the basis of the constructed cross-lingual parallel corpus of Chinese classic texts, we propose in this test the task of cross-lingual machine translation of Chinese classic texts.
 
# Participants
Researchers who are interested in machine translation and assisted machine translation of Chinese classic texts.

# Organizers
Li Bin, School of Chinese Language and Literature, Nanjing Normal University;
Wang Dongbo, College of Information Management, Nanjing Agricultural University; 
Shen Si, School of Economics and Management, Nanjing University of Science and Technology;
Feng Minxuan, School of Chinese Language and Literature, Nanjing Normal University;
Xu Chao, School of Chinese Language and Literature, Nanjing Normal University;
Zhao Lianzhen, School of Foreign Languages, Nanjing University of Chinese Medicine;
Sun Wenlong, School of Foreign Languages, Nanjing Tech University

# Data
The cross-lingual machine translation of Chinese classic texts consists of two parts: the Classical-Chinese-to-Modern-Chinese machine translation and the Classical-Chinese-to-English machine translation. The overall parallel texts for machine translation are presented as follows.
In this test, the cross-lingual parallel corpus of Chinese classic texts is large-scale, diachronic, and well-balanced. The Chinese classic texts in the corpus feature both diachronicity, i.e. spanning thousands of years, as well as diversity, i.e. covering the four traditional types of Chinese canonical texts: jing (经, Confucian classics), shi (史, historical works), zi (子, philosophical works belonging to schools of thought other than the Confucian but also including works on agriculture, medicine, mathematics, astronomy, divination, art criticism, and other miscellaneous writings) and ji (集, collection of literary works). Both English and modern Chinese translations are selected for these texts in the parallel corpus. The specific parallel texts provided for this test are as follows.

## Source
Classical-Chinese-to-Modern-Chinese parallel texts of China Twenty-four Histories
## Selecting criteria
Sentences of Chinese classic texts of seven characters or more in length
## Total data
322,473 sentence pairs in total; 9,583,749 characters for the original Chinese Classic texts and 12,763,534 characters for the Modern Chinese translations

## Source
Classical-Chinese-to-English parallel texts of Pre-Qin canonical texts and Zizhi Tongjian (资治通鉴, “Comprehensive Mirror in Aid of Governance”)
## Selecting criteria
Sentences of Chinese classic texts of seven characters or more in length and the corresponding English translations
## Total data
22,277 sentence pairs in total, including 618,083 characters in the original Classical Chinese texts and 838,321 words in the English translations

# Test Objective
Test the performance of the Classical-Chinese-to-English machine translation model and Classical-Chinese-to-Modern-Chinese machine translation model provided by the participants, based on BLEU (Bilingual Evaluation Understudy) and TER (Translation Error Rate).
