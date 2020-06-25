# 38. ヒストグラムPermalink
# 単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
# 縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
import re
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib


def parse(block):
    ret = []
    for row in block.split('\n'):
        rowlist = re.split(r'\t', row)
        if len(rowlist) == 2:
            rowarry = rowlist[1].split(',')
            lineDic = {
                'surface': rowlist[0],
                'base': rowarry[6],
                'pos': rowarry[0],
                'pos1': rowarry[1]
            }
            ret.append(lineDic)
    return ret


def getLongestNoun(x):
    return [y['base'] + '_' + y['pos'] + '_' + y['pos1'] for y in x]


filepath = 'neko.txt.mecab'
with open(filepath, encoding='utf-8') as f:
    block = f.read().split('EOS\n')
block = list(filter(lambda x: x != '', block))
result30 = [parse(y) for y in block]
result35 = [getLongestNoun(x) for x in result30]
dict = defaultdict(int)
for wordlist in result35:
    for word in wordlist:
        dict[word] += 1
result35 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
plt.figure(figsize=(8, 8))
print(dict.values())
plt.hist(dict.values(), bins=100)
plt.title('ヒストグラム')
plt.xlabel('出現頻度')
plt.ylabel('単語の種類数')
plt.xlim(xmin=1, xmax=400)
plt.show()
