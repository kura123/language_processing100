# 11. タブをスペースに置換Permalink
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
df.to_csv('result11.txt', sep=' ', header=None)
