# 33. 「AのB」Permalink
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
import re


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


def getnoun(x):
    ret = []
    for i in range(1, len(x) - 1):
        if x[i - 1]['pos'] == '名詞' and x[i]['surface'] == 'の' and x[i + 1]['pos'] == '名詞':
            ret.append(x[i - 1]['surface'] + x[i]['surface'] + x[i + 1]['surface'])
    return ret


filepath = 'neko.txt.mecab'
with open(filepath, encoding='utf-8') as f:
    block = f.read().split('EOS\n')
block = list(filter(lambda x: x != '', block))
result30 = [parse(y) for y in block]
result = [getnoun(x) for x in result30]
print(result)