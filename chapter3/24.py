# 24. ファイル参照の抽出Permalink
# 記事から参照されているメディアファイルをすべて抜き出せ．
import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
for media in re.findall(r'\[ファイル\s*:([^|]+)\|*.*?\]\]', text):
    print(media)
