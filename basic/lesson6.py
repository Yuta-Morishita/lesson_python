
# ! 文字列のメソッドを使ってみる

s = 'My name is Mike. Hi Mike'
print(s)

print(s.find('Mike'))
# ? 実行結果 11
# find()の文字列が何番目から始まるかを取得できる。

print(s.rfind('Mike'))
# ? 実行結果 20
# 後ろのMikeの文字列を取得している。

print(s.count('Mike'))
# ? 実行結果 2
# Mikeの文字列がいくつ含まれているか。

print(s.capitalize())
# ? 実行結果　My name is mike. hi mike
# 文字列の最初文字のみ大文字になる。

print(s.title())
# ? 実行結果 My Name Is Mike. Hi Mike
# 最初の文字が全て大文字になる。

print(s.upper())
# ? 実行結果 MY NAME IS MIKE. HI MIKE
# 全てが大文字になる。

print(s.lower())
# ? 実行結果　my name is mike. hi mike
# 全てが大文字になる。

print(s.replace('Mike', 'Nancy'))
# ? 実行結果 My name is Nancy. Hi Nancy
# MikeをNancyに置き換える。
