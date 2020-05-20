
# ! for break continue

some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1
    # ? 1 2 3 4 5

# ! 上記のコードをfor文で書く

for i in some_list:  # リストの中身を順に取り出すこと出来る。
    print(i)
    # ? 1 2 3 4 5
for word in ['My', 'name', 'is', 'Mike']:
    print(word)
    # ? MY
    # ? name
    # ? is
    # ? Mike


# ! for文の中で、breakを使う。
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)
    # ? MY

# ! for文の中で、continueを使う。

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)
    # ? MY
    # ? is
    # ? Mike

# ! for else文

for fruits in ['apple', 'banana', 'orange']:
    print(fruits)
else:
    print('I ate all!')
    # ? apple
    # ? banana
    # ? orange
    # ? I ate all!
