#coding = utf-8
import numpy as np


def load_corpus(filename):
    corpus = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            record = line.strip().split("\t")
            review = record[12] + " " + record[13]
            result = 1
            if record[11] in "Nn":
                result = 0
            corpus.append(review + "||" + str(result))
    return corpus


def load_dic(dic_file):
    dic = []
    with open(dic_file, "r", encoding="utf8") as f:
        for line in f:
            dic.append(line.strip())
    return dic


def modify_words(origin_word):
    font = []
    word = ''
    if ">" in origin_word:
        origin_word = origin_word.split(">")[1]
    if "<" in origin_word:
        origin_word = origin_word.split("<")[0]
    for letter in origin_word:
        if letter in "abcdefghijklmnopqrstuvwxyz'":
            word += letter
        if letter in "!.?":
            font.append(letter)
    return word, font


def load_weights(weights_file, dic):
    weights = np.zeros([len(dic), 2], dtype=float)
    count = 0
    with open(weights_file, "r", encoding="utf8") as f:
        for line in f:
            weight1, weight2 = line.strip().split()
            weights[count][0] = float(weight1)
            weights[count][1] = float(weight2)
            count += 1
    return weights


def build_dic(corpus, save_file):
    sf = open(save_file, "w+", encoding="utf8")
    dic = []
    num = 0
    for line in corpus:
        num += 1
        if num % 1000 == 0:
            print("{} lines processed.".format(num))
        sen, _ = line.strip().split("||")
        words = sen.split()
        for word in words:
            word = word.lower()
            word, font = modify_words(word)
            if word not in dic:
                dic.append(word)
            if len(font) > 0:
                for f in font:
                    if f not in dic:
                        dic.append(f)
    print("词汇表大小:{}".format(len(dic)))
    for word in dic:
        sf.write(word+"\n")
    sf.close()
    return dic


'''train_corpus = load_corpus("pacifier_train.tsv")
test_corpus = load_corpus("pacifier_test.tsv")
corpus = train_corpus + test_corpus
dic = build_dic(corpus, "dic.txt")'''


def train(corpus, save_path, dic):
    weight = np.zeros([len(dic), 2], dtype=float)
    save_f = open(save_path, "w+", encoding="utf8")
    pos_result = []
    neg_result = []
    for line in corpus:
        sen, label = line.strip().split("||")
        if label == "1":
            pos_result.append(sen.split())
        else:
            neg_result.append(sen.split())
    print("开始进行计算：")
    for i, word in enumerate(dic):
        if i % 1000 == 0:
            print("已经完成{}个词语的计算".format(i))
        p_count = 0
        n_count = 0
        for lis in pos_result:
            if word in lis:
                p_count += 1
        for lis in neg_result:
            if word in lis:
                n_count += 1
        weight[i][0] = float(p_count) / len(pos_result)
        weight[i][1] = float(n_count) / len(neg_result)
    for i in range(len(dic)):
        save_f.write(str(weight[i][0]) + " " + str(weight[i][1])+"\n")
    save_f.close()
    return weight


def pos_neg_num(corpus):
    pos_result = []
    neg_result = []
    for line in corpus:
        sen, label = line.strip().split("||")
        if label == "1":
            pos_result.append(sen.split("/"))
        else:
            neg_result.append(sen.split("/"))
    return len(pos_result), len(neg_result)


def test(corpus, weights, dic, t_corpus):
    pos_num, neg_num = pos_neg_num(t_corpus)
    total = 0
    correct = 0
    print("测试开始")
    for line in corpus:
        total += 1
        if total % 100 == 0:
            print("{}句已处理".format(total))
        sen, label = line.strip().split("||")
        origin_words = sen.split()
        actual_words = []
        for word in origin_words:
            if word in dic:
                actual_words.append(word)
        pos = np.log(pos_num)
        neg = np.log(neg_num)
        for word in actual_words:
            num = dic.index(word)
            if weights[num][0] != 0:
                pos += np.log(weights[num][0])
            if weights[num][1] != 0:
                neg += np.log(weights[num][1])
        if pos > neg:
            if label == "1":
                correct += 1
        else:
            if label == "0":
                correct += 1
    print(correct)
    print(total)
    print("准确率{}".format(float(correct)/total))
    return float(correct)/total


if __name__ == "__main__":
    train_corpus = load_corpus("hd_train.tsv")
    test_corpus = load_corpus("hd_test.tsv")
    dic = load_dic("hd_dic.txt")
    corpus = train_corpus + test_corpus
    #dic = build_dic(corpus, "hd_dic.txt")
    weight = train(train_corpus, "hd_weight.txt", dic)
    #weight = load_weights("pacifier_weight.txt", dic)
    test(test_corpus, weight, dic, train_corpus)