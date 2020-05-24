
# ! リスト内包表記

t = (1, 2, 3, 4, 5)
r = []
for i in t:
    r.append(i)

print(r)
# ? [1, 2, 3, 4, 5]
# タプルをリストないに展開をした。

# 一行で書くためには

r = [i for i in t]
print(r)
# ? [1, 2, 3, 4, 5]

t = (1, 2, 3, 4, 5)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)
# ? [2, 4]

# リストの中では、if文も使える。

r = [i for i in t if i % 2 == 0]
print(r)
# ? [2, 4]

# ! 辞書の内包表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)
# ? {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}

# ! 上記を内包表記する。

d = {x: y for x, y in zip(w, f)}
print(d)
# ? {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}

# ! 集合内表記

s = set()
for i in range(10):
    s.add(i)

print(s)
# ? {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


s = {i for i in range(10)}
print(s)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# ! ジェネレーター内包表記

def g():
    for i in range(10):
        yield i


g = g()
print(next(g))
print(next(g))
print(next(g))

# ? 0
# ? 1
# ? 2

# 内包表記

g = (i for i in range(10))
print(next(g))
print(next(g))
print(next(g))
# ? 0
# ? 1
# ? 2

