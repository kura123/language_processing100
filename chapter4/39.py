# 39. Zipfの法則Permalink
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
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
x = [x+1 for x in range(len(result35))]
y = [y[1] for y in result35]
plt.plot(x, y)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('単語の出現頻度順位',fontsize=14)
plt.ylabel('出現頻度を縦軸',fontsize=14)
plt.show()
