# 28. MediaWikiマークアップの除去Permalink
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
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
p6 = re.compile('\[\[([^]]+\||)(.+?)\]\]')
p7 = re.compile('<br />')
p8 = re.compile('\{\{([^}]+\||)(.*?)\}\}')
p9 = re.compile('\}\}.+$')

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
result26 = {k: p5.sub('', v) for k, v in res.items()}
result27 = {k:p6.sub(r'\2',v) for k,v in result26.items()}
result = {k:p7.sub('',v) for k,v in result27.items()}
result = {k:p8.sub(r'\2',v) for k,v in result.items()}
result = {k:p9.sub('',v) for k,v in result.items()}
print(result)