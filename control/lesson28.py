
# ! enumerate関数

i = 0
for fruits in ['apple', 'banana', 'orange']:
    print(i, fruits)
    i += 1
# ? 0 apple
# ? 1 banana
# ? 2 orange
# enumerateを使えば、上記のようにiを回す必要がない。

for i, fruits in enumerate(['apple', 'banana', 'orange']):
    print(i, fruits)
# ? 0 apple
# ? 1 banana
# ? 2 orange
