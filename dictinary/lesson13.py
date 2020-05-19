
# ! 辞書型の学習

d = {'x': 10, 'y': 20}
print(d)
# ? {'x': 10, 'y': 20}

print(type(d))
# ? <class 'dict'>

print(d['x'])
# ? 10

# 辞書に代入をする。
d['x'] = 100
print(d)
# ? {'x': 100, 'y': 20}

d['z'] = 300
print(d)
# ? {'x': 100, 'y': 20, 'z': 300}

c = dict(a=10, b=20)
print(c)
# ? {'a': 10, 'b': 20}
# dictを使っても、辞書の作成ができる。
