
# ! 辞書をfor文で出力する。

d = {'x': 100, 'y': 200}

for v in d:
    print(v)
# ? x
# ? y
# keyのみが取り出せる。

# keyとvalueの両方を出力したい場合。

for k, v in d.items():
    print(k, ':', v)
# ? x  100
# ? y : 200
