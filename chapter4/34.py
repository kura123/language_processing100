# 34. 名詞の連接Permalink
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
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


def getLongestNoun(x):
    ret = []
    noun = []
    for y in x:
        if y['pos'] == '名詞':
            noun.append(y['surface'])
        elif len(noun) > 1:
            ret.append(''.join(noun))
            noun = []
        else:
            noun = []
    return ret


filepath = 'neko.txt.mecab'
with open(filepath, encoding='utf-8') as f:
    block = f.read().split('EOS\n')
block = list(filter(lambda x: x != '', block))
result30 = [parse(y) for y in block]
result = [getLongestNoun(x) for x in result30]
print(result)
