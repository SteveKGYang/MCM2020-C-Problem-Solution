#encoding = utf-8

import numpy as np
import matplotlib.pyplot as plt


class Enhanced_Randomwalking:
    def __init__(self):
        self.present_position = 0
        self.origin_distribution = np.array([.5, .5])
        self.origin_trans = np.array([[.6, .4], [.3, .7]])

    def markov_modify(self, star, useful, total):
        if useful != 0 and total != 0:
            if star == 1 or star == 2:
                star -= 0.5 * float(useful) / total
            if star == 4 or star == 5:
                star += 0.5 * float(useful) / total
        if useful == 0 and total != 0:
            if star == 1 or star == 2:
                star += 0.5
            if star == 4 or star == 5:
                star -= 0.5
        self.origin_trans[0][0] += 0.05 * star
        self.origin_trans[0][1] -= 0.05 * star
        self.origin_trans[1][0] += 0.05 * star
        self.origin_trans[1][1] -= 0.05 * star

    def update_prob(self):
        self.origin_distribution = np.dot(self.origin_distribution, self.origin_trans)

    def restore_trans(self):
        self.origin_trans = np.array([[.6, .4], [.3, .7]])

    def random_walking(self):
        up_prob = self.origin_distribution[0]/np.sum(self.origin_distribution)
        k = np.random.rand()
        if k < up_prob:
            self.present_position += 1
        else:
            self.present_position -= 1
        return self.present_position

    def restore(self):
        self.origin_distribution = np.array([.5, .5])
        self.origin_trans = np.array([[.6, .4], [.3, .7]])


def get_month(time):
    return time.strip().split("/")[0]


def random_walking(filename):
    er = Enhanced_Randomwalking()
    corpus = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f:
            record = line.strip().split("\t")
            corpus.append(record)
    corpus.reverse()
    i = 0
    corpus_len = len(corpus)
    result = [0]
    ave_ratings = []
    while i < corpus_len:
        present_set = []
        month = get_month(corpus[i][0])
        while get_month(corpus[i][0]) == month:
            present_set.append(corpus[i])
            i += 1
            if i >= corpus_len:
                break
        ratings = 0
        for record in present_set:
            star = int(record[2])
            useful = int(record[3])
            total = int(record[4])
            ratings += star
            er.markov_modify(star, useful, total)
            er.update_prob()
            er.restore_trans()
        result.append(er.random_walking())
        ave_ratings.append(float(ratings)/len(present_set))
        er.restore()
    return result, ave_ratings



result, ave_ratings = random_walking("micro_longest.tsv")
x = np.arange(0, len(result), 1)
z = np.arange(1, len(result), 1)
y = np.array(result)
print(x)
print(y)
plt.plot(x, y, label='Reputation')
plt.plot(z, ave_ratings, label='Average Star')
plt.xlabel('Months')
plt.ylabel('Reputation/Average Stars')
plt.title('Product 423421857 Reputation Simulation')
plt.legend()
plt.show()




