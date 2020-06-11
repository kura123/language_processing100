# 04. 元素記号Permalink
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King
# Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
string = string.replace(',', '').replace('.', '')
words = [word for word in string.split()]
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
map = {}
for i, name in enumerate(words, 1):
    if i in index:
        s = name[:1]
    else:
        s = name[:2]
    map[i] = s
print(map)
