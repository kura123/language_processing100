# 37. 「猫」と共起頻度の高い上位10語Permalink
# 「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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
list = list(filter(lambda x: '猫_名詞_一般' in x, result35))
dict = defaultdict(int)
for wordlist in list:
    for word in wordlist:
        if word != '猫_名詞_一般':
            dict[word] += 1
result = sorted(dict.items(), key=lambda x: x[1], reverse=True)
labels = [la[0] for la in result[:10]]
values = [va[1] for va in result[:10]]
plt.figure(figsize=(10, 8))
plt.barh(labels, values)
plt.show()
