# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(df[0].value_counts())