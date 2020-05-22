
# ! 位置引数とキーワード引数とデフォルト引数

# ! 複数の引数を与える。


def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu('beef', 'beer', 'ice')  # 左から順番に、引数に入る。
# ? beef
# ? beer
# ? ice


def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu('beef', 'ice', 'beer')
# ? beef
# ? ice
# ? beer
# ? 引数の順番が違うと、結果も変わってしまう。


# 上記のような間違いをなくすには、アーギュメントキーワードを利用する。
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu(entree='beef', dessert='ice', drink='beer')
# ? beef
# ? beer
# ? ice


# ! デフォルト引数。

def menu(entree='beef', drink='beer', dessert='desert'):  # デフォルトの引数を与える
    print(entree)
    print(drink)
    print(dessert)


menu()
# ? beef
# ? beer
# ? ice


def menu(entree='beef', drink='beer', dessert='desert'):  # デフォルトの引数を与える
    print(entree)
    print(drink)
    print(dessert)


menu(entree='chickin')  # 　デフォルト引数を書き換えることが出来る。
# ? chickin
# ? beer
# ? ice
