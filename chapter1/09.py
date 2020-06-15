# 09. TypoglycemiaPermalink
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラム
# を作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば”I couldn’t believe that I could actually understand what I was reading :
# the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
import random

def chengeWord(w):
    if len(w) >4:
        middle = list(w[1:-1])
        random.shuffle(middle)
        return w[0]+''.join(middle)+w[-1]
    else:
        return w

string = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(' '.join([chengeWord(word) for word in string.split()]))