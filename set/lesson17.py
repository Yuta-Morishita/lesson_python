
# ! 集合型の学習

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
# ? {1, 2, 3, 4, 5, 6} 辞書と同じ{}を利用するがユニークになっている。
print(type(a))
# ? <class 'set'>

b = {2, 3, 3, 6, 7}
print(b)
# ? {2, 3, 6, 7}

print(a-b)
# ? {1, 4, 5}
# 重複している値が取り除かれる。

print(b - a)
# ? {7}

print(a & b)
# ? {2, 3, 6}
# 共に共通するものを取り出せる

print(a | b)
# aとbの全てを取り出せる。

print(a ^ b)
# ? {1, 4, 5, 7}
# aとbの中に存在するが、重複をしてないもの。
