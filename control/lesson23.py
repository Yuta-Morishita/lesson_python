
# ! while文とcontinue文とbreak文


# ! while文
count = 0

while count < 5:
    print(count)
    count += 1
# ? 0 1 2 3 4

# ! break文

count = 0
while True:
    if count >= 5:
        break  # if判定にヒットしたwhile文を抜ける。
    print(count)
    count += 1
# ? 0 1 2 3 4

# ! continue

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue  # if文にヒットしたら、while文に戻る。
    print(count)  # if文にヒットしたらプリントが出力されない。
    count += 1
# ? 0 1 3 4
