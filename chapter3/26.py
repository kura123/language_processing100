# 26. 強調マークアップの除去Permalink
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去して
# テキストに変換せよ（参考: マークアップ早見表）
import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
p = re.compile('\|(.*?)=(.*?)$')
p1 = re.compile('\{\{\s*基礎情報')
p2 = re.compile('\}\}')
p3 = re.compile('\|')
p4 = re.compile('<ref[^>]*>.*?(</ref>|$)')
#除去用パターン
p5 = re.compile("'+")
ls = []
flag = False

for l in text.split('\n'):
    if flag:
        ml = [p2.match(l), p3.match(l)]
        if ml[0]:
            break
        if ml[1]:
            ls.append(p4.sub('', l))
    if p1.match(l):
        flag = True
res = {b.group(1).strip(): b.group(2).strip() for b in [p.match(a) for a in ls]}
result = {k: p5.sub('', v) for k, v in res.items()}
print(res)
