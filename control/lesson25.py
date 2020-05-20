
# ! input関数

while True:
    word = input('Enter')  # stringで取得する。
    if word == 'ok':
        break
    print('next')
    # okが入力されるまで、nextが繰り返し表示される。


# integerで取得
while True:
    word = input('Enter')
    num = int(word)
    if num == 100:
        break
    print('next')
