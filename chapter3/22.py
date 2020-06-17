# 22. カテゴリ名の抽出Permalink
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
text = text.split('\n')
row = list(filter(lambda x: '[Category:' in x, text))
result = [re.sub(r'\[\[Category:|\|\*|]]', '', y) for y in row]
print(result)
