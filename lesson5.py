
# ! 文字列のインデックス　スライスの学習　文字列に長さを取得

# ! インデックス
word = 'Python'  # 左から順番に０から番号を振られる。
print(word[0])
# ? 出力結果　P　
print(word[1])
# ? 出力結果　y
# 1は左から２番目のyである。

print(word[-1])
# ? 出力結果　n
# -1をすると最後の文字を出力する。

print(word[-2])
# ? 出力結果 0

# ! スライス
print(word[0:2])
# ? 出力結果　Py
# 0と１の文字列が取得できる
print(word[:2])  # でも同様の文字列取得する。


print(word[2:5])
# ? 出力結果 tho
# 2 3 4 のインデックスを持つ文字列が出力される。

print(word[2:])
# ? 出力結果 thon
# 2から最後の文字列までを取得する。

# ! 文字列を書き換える
word = 'j' + word[1:]  # jをwordの文字列、０番目以降に足す。
print(word)
# ? 出力結果 jython


# ! 文字列の長さを取得する
n = len(word)
print(n)
# ? 出力結果 6 jythonの文字列の長さを取得出来ている。