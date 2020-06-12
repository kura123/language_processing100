# 06. 集合Permalink
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
def n_gram(s, i):
    re = []
    for j in range(len(s) - i + 1):
        re.append(s[j:j + i])
    return re


string1 = 'paraparaparadise'
string2 = 'paragraph'
X = set(n_gram(string1, 2))
Y = set(n_gram(string2, 2))

print('和集合')
print(X | Y)
print('積集合')
print(X & Y)
print('差集合')
print(X - Y)
print('Xにseが含まれているか')
print('se' in X)
print('Yにseが含まれているか')
print('se' in Y)
