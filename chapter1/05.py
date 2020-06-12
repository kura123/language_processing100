# 05. n-gramPermalink
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から
# 単語bi-gram，文字bi-gramを得よ．
def n_gram(s, i):
    re = []
    for j in range(len(s) - i + 1):
        re.append(s[j:j + i])
    return re


string = 'I am an NLPer'
word = string.split()
print(n_gram(string, 2))
