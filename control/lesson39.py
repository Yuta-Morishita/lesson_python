
# ! ラムダ
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))  # funcでsample_funcが呼び出される。


def sample_func(word):
    return word.capitalize()  # 先頭の文字を大文字にして返す。


change_words(l, sample_func)  # 引数に配列のlと関数であるsample_funcを入れる。
# ? Mon
# ? Tue
# ? Wed
# ? Thu
# ? Fri
# ? Sat
# ? Sun

# ! ラムダを使うと一行で書ける。
# def sample_func(word):
# return word.capitalize() この部分が書ける。


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word): return word.capitalize()


change_words(l, sample_func)  # 引数にlambda word: word.capitalize()を渡すことが出来る。
# ? Mon
# ? Tue
# ? Wed
# ? Thu
# ? Fri
# ? Sat
# ? Sun
