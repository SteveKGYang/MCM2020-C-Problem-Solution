# coding:utf-8
from tools import balance
import naive_bayes
import random


def build_set(corpus, divide_num, size, filename):
    pos_ratio = balance(filename)
    pos_corpus = []
    neg_corpus = []
    for line in corpus:
        sen, label = line.strip().split("||")
        if label == "1":
            pos_corpus.append(line.strip())
        else:
            neg_corpus.append(line.strip())
    final_corpus = []
    pos_num = int(size * pos_ratio)
    neg_num = size - pos_num
    pos_pointer = 0
    neg_pointer = 0
    for i in range(divide_num - 1):
        new_corpus = []
        for j in range(pos_pointer, pos_pointer + pos_num):
            new_corpus.append(pos_corpus[j])
        for j in range(neg_pointer, neg_pointer + neg_num):
            new_corpus.append(neg_corpus[j])
        random.shuffle(new_corpus)
        pos_pointer += pos_num
        neg_pointer += neg_num
        final_corpus.append(new_corpus)
    new_corpus = []
    for j in range(pos_pointer, len(pos_corpus)):
        new_corpus.append(pos_corpus[j])
    for j in range(neg_pointer, len(neg_corpus)):
        new_corpus.append(neg_corpus[j])
    final_corpus.append(new_corpus)
    print(len(final_corpus))
    for co in final_corpus:
        print("数据集大小{}".format(len(co)))
    return final_corpus


def cross_validation(filename, divide_num, size):
    corpus = naive_bayes.load_corpus(filename)
    dic = naive_bayes.build_dic(corpus, "microwave_dic.txt")
    divided_corpus = build_set(corpus, divide_num, size, filename)
    accs = []
    for i in range(divide_num):
        train_corpus = []
        test_corpus = divided_corpus[i]
        for j in range(divide_num):
            if j != i:
                train_corpus += divided_corpus[j]
        weight = naive_bayes.train(train_corpus, "microwave_weight.txt", dic)
        test_acc = naive_bayes.test(test_corpus, weight, dic, train_corpus)
        accs.append(test_acc)
    print(accs)
    print("最终的准确率平均值：{}".format(sum(accs)/divide_num))


if __name__ == "__main__":
    cross_validation("microwave.tsv", 8, 200)
