
# ! 引数のタプル化


def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)


say_something('Hi', 'Mike', 'Nancy')
# ? Hi
# ? Mike
# ? Nancy

# 上記のコードをまとめることが出来る。


def say_something(*args):
    print(args)


say_something('Hi', 'Mike', 'Nancy')
# ? ('Hi', 'Mike', 'Nancy')
# 引数をタプル化してくれる。


def say_something(*args):  # 引数がいくつ入ってくるかわからない時などに、使用する。
    for arg in args:
        print(arg)


say_something('Hi', 'Mike', 'Nancy')
# ? Hi
# ? Mike
# ? Nancy
