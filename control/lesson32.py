
# ! 関数の定義


def say_something():
    print('hi')


say_something()  # 関数を呼び出す
# ? hi

# ! 返り値


def say_something2():
    s = 'hihi'  # 文字列をsに代入
    return s  # 関数にsを返す。


result = say_something2()  # 返ってきたsが代入された関数をresultに代入する。
print(result)
# ? hihi


# ! 引数を使う。

def what_is_this(color):  # 呼び出された関数にredが入っている。
    print(color)


what_is_this('red')  # 関数を呼び出す際に、文字列を渡す。
# ? red


def what_is_this2(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this2('green')
print(result)

# ? green pepper
