# 13. col1.txtとcol2.txtをマージPermalink
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．
import pandas as pd

col1 = pd.read_csv('col1.txt', sep='\t', header=None)
col2 = pd.read_csv('col2.txt', sep='\t', header=None)

df = pd.concat([col1, col2], axis=1)
df.to_csv('result13.txt', sep='\t', index=False, header=None)
