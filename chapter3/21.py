# 21. カテゴリ名を含む行を抽出Permalink
# 記事中でカテゴリ名を宣言している行を抽出せよ．
import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df. query('title=="イギリス"')['text'].values[0]
text = text.split('\n')
result = list(filter(lambda x: 'Category:' in x, text))
print(result)