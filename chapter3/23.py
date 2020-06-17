# 23. セクション構造Permalink
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
section = re.findall(r'(=+)([^=]+)\1\s*\n', text)
for i in section:
    print(i[1].strip() + '\t' + str(len(i[0]) - 1))
