# coding=utf-8
import random


def balance(filename):
    positive = 0
    negative = 0
    total = 0
    wrong = 0
    with open(filename, "r", encoding="utf8") as f:
        for num, line in enumerate(f):
            if num != 0:
                record = line.strip().split("\t")
                #print(record[11])
                if record[11] == "Y" or record[11] == "y":
                    positive += 1
                elif record[11] == "N" or record[11] == "n":
                    negative += 1
                else:
                    wrong += 1
                    print(record[11])
                total += 1
    print("正例所占比例{}".format(float(positive)/total))
    return float(positive)/total


def bulid_dataset(origin_file, out_name):
    positive = []
    negative = []
    with open(origin_file, "r", encoding="utf8") as f:
        for num, line in enumerate(f):
            if num != 0:
                record = line.strip().split("\t")
                if record[11] == "Y" or record[11] == "y":
                    positive.append(record)
                elif record[11] == "N" or record[11] == "n":
                    negative.append(record)
    tf = open(out_name+"_train.csv", "w+", encoding="utf8")
    tef = open(out_name+"_test.csv", "w+", encoding="utf8")
    tra_set = []
    tes_set = []
    if len(positive) > 7650:
        for i in range(7650):
            tra_set.append("\t".join(positive[i]))
        for i in range(7650, len(positive)):
            tes_set.append("\t".join(positive[i]))
    else:
        print("Wrong")

    if len(negative) > 1350:
        for i in range(1350):
            tra_set.append("\t".join(negative[i]))
        for i in range(1350, len(negative)):
            tes_set.append("\t".join(negative[i]))
    print("训练集大小：{}".format(len(tra_set)))
    print("测试集大小：{}".format(len(tes_set)))
    print("源数据大小：{}".format(len(positive)+len(negative)))
    random.shuffle(tra_set)
    random.shuffle(tes_set)

    for line in tra_set:
        tf.write(line+"\n")
    for line in tes_set:
        tef.write(line+"\n")
    tf.close()
    tef.close()


def find_longest_product(filename, write_file):
    corpus = {}
    sens = []
    with open(filename, "r", encoding="utf8") as f:
        for i, line in enumerate(f):
            if i != 0:
                record = line.strip().split("\t")
                sens.append(record)
                re = record[4].strip()
                if re in corpus.keys():
                    corpus[re] += 1
                else:
                    corpus[re] = 1
    max_num = 0
    max_parent = ''
    longest_product = []
    for parent, num in corpus.items():
        if num > max_num:
            max_parent = parent
            max_num = num
    if max_parent != '':
        for sen in sens:
            if sen[4] == max_parent:
                #s = sen[len(sen)-1] + "\t" + sen[4] + "\t" + sen[7] + "\t" + sen[8] + "\t" + sen[9]
                s = sen[7] + "\t" + sen[11]
                longest_product.append(s)
        with open(write_file, "w+", encoding="utf8") as f:
            for line in longest_product:
                f.write(line + "\n")
    else:
        print("Wrong.")
    return longest_product

find_longest_product("./Problem_C_Data/microwave.tsv", "./CRF_file/micro    _longest.csv")

