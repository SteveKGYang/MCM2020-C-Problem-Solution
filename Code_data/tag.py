#encoding = utf-8

import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown
import numpy as np
import matplotlib.pyplot as plt

'''text = "I am very disappointed.".lower()
text_list = nltk.word_tokenize(text)
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
text_list = [word for word in text_list if word not in english_punctuations]
stops = set(stopwords.words("english"))
text_list = [word for word in text_list if word not in stops]


print(nltk.pos_tag(text_list))'''


def tag():
    hd_pos = []
    hd_neg = []
    with open("./Problem_C_Data/hair_dryer.tsv", encoding="utf8") as f:
        for line in f:
            record = line.strip().split("\t")
            if record[7] == '5':
                hd_pos.append(record[12])
                hd_pos.append(record[13])
            if record[7] == '1':
                hd_neg.append(record[12])
                hd_neg.append(record[13])
    paci_pos = []
    paci_neg = []
    with open("./Problem_C_Data/pacifier.tsv", encoding="utf8") as f:
        for line in f:
            record = line.strip().split("\t")
            if record[7] == '5':
                paci_pos.append(record[12])
                paci_pos.append(record[13])
            if record[7] == '1':
                paci_neg.append(record[12])
                paci_neg.append(record[13])
    micro_pos = []
    micro_neg = []
    with open("./Problem_C_Data/microwave.tsv", encoding="utf8") as f:
        for line in f:
            record = line.strip().split("\t")
            if record[7] == '5':
                micro_pos.append(record[12])
                micro_pos.append(record[13])
            if record[7] == '1':
                micro_neg.append(record[12])
                micro_neg.append(record[13])

    '''hd_pos_dict = {}
    hd_neg_dict = {}
    for text in hd_pos:
        text = text.lower()
        text_list = nltk.word_tokenize(text)
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]

        for word, seg in nltk.pos_tag(text_list):
            if seg.strip() == 'JJ' or seg.strip() == 'JJR' or seg.strip() == 'JJS':
                if word.strip() in hd_pos_dict.keys():
                    hd_pos_dict[word] += 1
                else:
                    hd_pos_dict[word] = 1

    for text in hd_neg:
        text = text.lower()
        text_list = nltk.word_tokenize(text)
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]

        for word, seg in nltk.pos_tag(text_list):
            if seg.strip() == 'JJ' or seg.strip() == 'JJR' or seg.strip() == 'JJS':
                if word.strip() in hd_neg_dict.keys():
                    hd_neg_dict[word] += 1
                else:
                    hd_neg_dict[word] = 1
        with open("./words/hd_pos.txt", "w+", encoding="utf8") as f:
            for word in hd_pos_dict.keys():
                f.write(word+" "+str(hd_pos_dict[word])+"\n")
        with open("./words/hd_neg.txt", "w+", encoding="utf8") as f:
            for word in hd_neg_dict.keys():
                f.write(word+" "+str(hd_neg_dict[word])+"\n")'''

    paci_pos_dict = {}
    paci_neg_dict = {}
    for text in paci_pos:
        text = text.lower()
        text_list = nltk.word_tokenize(text)
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]

        for word, seg in nltk.pos_tag(text_list):
            if seg.strip() == 'JJ' or seg.strip() == 'JJR' or seg.strip() == 'JJS':
                if word.strip() in paci_pos_dict.keys():
                    paci_pos_dict[word] += 1
                else:
                    paci_pos_dict[word] = 1

    for text in paci_neg:
        text = text.lower()
        text_list = nltk.word_tokenize(text)
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]

        for word, seg in nltk.pos_tag(text_list):
            if seg.strip() == 'JJ' or seg.strip() == 'JJR' or seg.strip() == 'JJS':
                if word.strip() in paci_neg_dict.keys():
                    paci_neg_dict[word] += 1
                else:
                    paci_neg_dict[word] = 1
        with open("./words/paci_pos.txt", "w+", encoding="utf8") as f:
            for word in paci_pos_dict.keys():
                f.write(word + " " + str(paci_pos_dict[word]) + "\n")
        with open("./words/paci_neg.txt", "w+", encoding="utf8") as f:
            for word in paci_neg_dict.keys():
                f.write(word + " " + str(paci_neg_dict[word]) + "\n")

    micro_pos_dict = {}
    micro_neg_dict = {}
    for text in micro_pos:
        text = text.lower()
        text_list = nltk.word_tokenize(text)
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]

        for word, seg in nltk.pos_tag(text_list):
            if seg.strip() == 'JJ' or seg.strip() == 'JJR' or seg.strip() == 'JJS':
                if word.strip() in micro_pos_dict.keys():
                    micro_pos_dict[word] += 1
                else:
                    micro_pos_dict[word] = 1

    for text in micro_neg:
        text = text.lower()
        text_list = nltk.word_tokenize(text)
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]

        for word, seg in nltk.pos_tag(text_list):
            if seg.strip() == 'JJ' or seg.strip() == 'JJR' or seg.strip() == 'JJS':
                if word.strip() in micro_neg_dict.keys():
                    micro_neg_dict[word] += 1
                else:
                    micro_neg_dict[word] = 1
        with open("./words/micro_pos.txt", "w+", encoding="utf8") as f:
            for word in micro_pos_dict.keys():
                f.write(word + " " + str(micro_pos_dict[word]) + "\n")
        with open("./words/micro_neg.txt", "w+", encoding="utf8") as f:
            for word in micro_neg_dict.keys():
                f.write(word + " " + str(micro_neg_dict[word]) + "\n")


def rank(filename):
    corpus = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            record = line.strip().split(" ")
            corpus.append(record)
    rank = []
    print(len(corpus))
    for i in range(20):
        max_num = 0
        re = None
        for record in corpus:
            if int(record[1]) > max_num:
                max_num = int(record[1])
                re = record
        rank.append(re)
        corpus.remove(re)
    print(rank)


def drawPillar():
    n_groups = 6
    means_men = (4825, 2035, 942, 30, 30, 15)
    means_women = (330, 30, 30, 327, 285, 450)

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    rects1 = plt.bar(index, means_men, bar_width, alpha=opacity, color='b', label='5 Star')
    rects2 = plt.bar(index + bar_width, means_women, bar_width, alpha=opacity, color='r', label='1 Star')

    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Histogram of Frequency of Quality Descriptors')
    plt.xticks(index + bar_width, ('Great', 'Easy', 'Perfect', 'Disappointed', 'Hard', 'Horrible'))
    plt.ylim(0, 5000)
    plt.legend()

    plt.tight_layout()
    plt.show()

rank("./words/paci_pos.txt")
rank("./words/paci_neg.txt")
#drawPillar()