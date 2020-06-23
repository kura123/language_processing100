# 31. 動詞Permalink
# 動詞の表層形をすべて抽出せよ．
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

def getVerb(x, tirget):
    ret = list(filter(lambda y: y['pos'] == '動詞', x))
    ret = [z[tirget] for z in ret]
    return ret

filepath = 'neko.txt.mecab'
with open(filepath, encoding='utf-8') as f:
    block = f.read().split('EOS\n')
block = list(filter(lambda x: x != '', block))
result30 = [parse(y) for y in block]
result = [getVerb(x, 'surface') for x in result30]
print(result)
