# ! 変数宣言の学習


num = 100
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))  # boolean型は真偽値を保存するための型

# pythonは変数の型を独自で判断する
# type関数を使用することで、型の種類を見ることができる。

# ? 型変換

num = 1
name = '1'

new_num = int(name)

print(new_num, type(new_num))

# ? 3.6以上の書き方

num: int = 1
name: str = 'Mike'
print(num, type(num))
print(name, type(name))
