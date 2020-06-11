# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

string1 = 'パトカー'
string2 = 'タクシー'
print (''.join([a+b for a,b in zip(string1,string2)]))