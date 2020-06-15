# 08. 暗号文Permalink
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(S):
    new = []
    for s in S:
        if 97 <= ord(s) <= 122:
            s = chr(219 - ord(s))
        new.append(s)
    return ''.join(new)

string = 'I am an NLPer'
new = cipher(string)
print (new)
print (cipher(new))