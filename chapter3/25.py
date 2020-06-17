# 25. テンプレートの抽出Permalink
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
p = re.compile('\|(.*?)=(.*?)$')
p1 = re.compile('\{\{\s*基礎情報')
p2 = re.compile('\}\}')
p3 = re.compile('\|')
p4 = re.compile('<ref\s*>.*?(</ref>|$)')
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
print(res)
