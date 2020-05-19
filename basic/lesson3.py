
# ! printで出力することを学習

print('Hi')
# ? 出力結果　Hi

print('Hi', 'Mike')
# ? 出力結果　Hi Mike

print('Hi', 'Mike', sep=',')
# ? 出力結果　Hi,Mike
# spc=''(セパレーション)の中で区切ることができる。

print('Hi', 'Mike', sep=',', end='.')
# ? 出力結果　Hi,Mike.
# printした文字の末尾に付け足すことができる。

# \nを入れると改行ができる
print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Emily', sep=',', end='.')
# ? 出力結果　Hi,Mike.
# ?         Hi,Emily.

print('Hi', 'Mike', sep=',', end='.')
print('Hi', 'Emily', sep=',', end='.')
# ? 出力結果　Hi,Mike.Hi,Emily.
