# 29. 国旗画像のURLを取得するPermalink
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
import pandas as pd
import re
import requests

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
p = re.compile('\|(.*?)=(.*?)$')
p1 = re.compile('\{\{\s*基礎情報')
p2 = re.compile('\}\}')
p3 = re.compile('\|')
p4 = re.compile('<ref[^>]*>.*?(</ref>|$)')
# マークアップ除去用パターン
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
#マークアップ除去
result26 = {k: p5.sub('', v) for k, v in res.items()}
result27 = {k: p6.sub(r'\2', v) for k, v in result26.items()}
result = {k: p7.sub('', v) for k, v in result27.items()}
result = {k: p8.sub(r'\2', v) for k, v in result.items()}
result = {k: p9.sub('', v) for k, v in result.items()}


S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
title = re.sub(r' ', '_', result['国旗画像'])
PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:" + title,
    "iiprop": "url"
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
resultURl = ''
for k, v in DATA['query']['pages'].items():
    resultURl = v['imageinfo'][0]['url'] if 'imageinfo' in v else resultURl

print(resultURl)
