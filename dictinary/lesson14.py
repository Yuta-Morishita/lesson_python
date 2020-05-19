# ! 辞書型のメソッド

d = {'x': 10, 'y': 20}
print(d)

# keyを取得する
print(d.keys())
# ? dict_keys(['x', 'y'])

# valueを取得する
print(d.values())
# ? dict_values([10, 20])

# 辞書の上書き
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)
# ? {'x': 1000, 'y': 20, 'j': 500}

# getを使ってvalueを取得する
print(d.get('x'))
# ? 1000
