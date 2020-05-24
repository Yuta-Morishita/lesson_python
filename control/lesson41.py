
# ! ジェネレーター

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)
# ? Good morning
# ? Good afternoon
# ? Good night


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


for g in greeting():
    print(g)

    # ? Good morning
    # ? Good afternoon
    # ? Good night
    # 結果的には上のコードと同じ結果となる

# ! どんな場面で使用するのか


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
print(next(g))

print('@@@@@@@@@@@')

print(next(g))

print('@@@@@@@@@@@')

print(next(g))

# ? Good morning
# ? @@@@@@@@@@@
# ? Good afternoon
# ? @@@@@@@@@@@
# ? Good night

# ジェネレータの場合は、nextでyieldを呼び出した後に、一度関数から抜ける。
