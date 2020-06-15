# 15. 末尾のN行を出力Permalink
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
import sys
import pandas as pd

if len(sys.argv) != 1:
    n = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    print(df.tail(n))
else:
    print('引数ない')
