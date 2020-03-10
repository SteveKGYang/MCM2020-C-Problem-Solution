#encoding = utf-8
import numpy as np


def crf(filename, cen0, cen1, para1, para2, para3, N):
    stars = []
    purchases = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f:
            star, purchase = line.strip().split("\t")
            stars.append(int(star))
            if purchase in 'Yy':
                purchases.append(1)
            else:
                purchases.append(0)
    stars.reverse()
    purchases.reverse()

    predict_result = []
    for i in range(len(purchases)):
        sentiment0 = 1 - purchases[i]
        sentiment1 = purchases[i]
        if np.random.rand() < 0.1:
            sentiment1 = 1 - sentiment1
            sentiment0 = 1 - sentiment0
        dis0 = abs(cen0 - stars[i])
        dis1 = abs(cen1 - stars[i])
        purchase_rate0 = 0.5
        purchase_rate1 = 0.5
        sums = 0
        for j in range(max(i-N, 0), i):
            sums += purchases[j]
        if sums != 0:
            purchase_rate1 = float(sums) / N
            purchase_rate0 = 1 - purchase_rate1
        pos = sentiment1 * para1 + dis1 * para2 + purchase_rate1 * para3
        neg = sentiment0 * para1 + dis0 * para2 + purchase_rate0 * para3
        t = np.exp(pos) + np.exp(neg)
        pos_prob = np.exp(pos) / t
        neg_prob = np.exp(neg) / t
        if pos_prob > neg_prob:
            predict_result.append(1)
        else:
            predict_result.append(0)

    acc = .0
    TP = .0
    FP = .0
    FN = .0
    for predict, an in zip(predict_result, purchases):
        if predict == an:
            acc += 1
        if predict == an == 1:
            TP += 1
        if predict == 0 and an == 1:
            FP += 1
        if predict == 1 and an == 0:
            FN += 1
    pre = TP/(TP+FP)
    re = TP/(TP+FN)
    f1 = 2 * pre * re / (pre + re)
    print("Acc:{} Precision:{} Recall:{} F1:{}".format(acc/len(purchases), pre, re, f1))
    print(2*acc/len(purchases)*pre/(acc/len(purchases)+pre))

crf("./CRF_file/hd_longest.tsv", 2.172, 4.763, 1.0, 0.3, 0.9, 10)
