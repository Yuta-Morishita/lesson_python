
# ! タプルの学習

# タプルはデータの書き込みが出来ないために、
# 後にデータの中身を書き換えられたくないデータを代入するのに適している。

t = (1, 2, 3, 4, 5)
print(type(t))
# ? <class 'tuple'>
print(t)
# ? (1, 2, 3, 4, 5)


# ! タプルのアンパッキング

num_tuple = (10, 20)
print(num_tuple)
# ? (10, 20)

x, y = num_tuple
print(x, y)
# ? 10 20
# タプルの中身がx yに展開されている。

# ! タプルの使いどころ

# 問題の答えなどをタプルに代入すると便利。
chose_from_two = ('a', 'b', 'c')

# 利用者の回答を空のリストに代入する。
answer = []

answer.append('a')
chose_from_two.append('b')  # ! 仮にリストを使用していた場合、こちらのコードで答えの中身が書き換えられてしまう。

print(chose_from_two)
print(answer)
