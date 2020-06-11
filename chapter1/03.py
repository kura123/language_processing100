# 03. 円周率Permalink
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
string = string.replace(',','').replace('.','')
result = [len(word) for word in string.split()]
print(result)