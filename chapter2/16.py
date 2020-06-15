# 16. ファイルをN分割するPermalink
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．
import sys
import pandas as pd

if len(sys.argv) != 1:
    n = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    row = len(df) // n
    print(row)
else:
    print('引数ない')
    exit();

for i in range(n):
    df.loc[row * i:row * (i + 1)].to_csv(f'result16_{i}.txt', sep='\t', index=False, header=None)
