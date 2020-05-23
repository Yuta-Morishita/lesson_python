
# ! キーワード引数の辞書化


def menu(entree='beef', drink='wine'):
    print(entree, drink)


menu(entree='beef', drink='coffee')
# ? beef coffee


def menu(**kwargs):
    print(kwargs)


menu(entree='beef', drink='coffee')
# ? {'entree': 'beef', 'drink': 'coffee'}
# 辞書として渡される。


def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


menu(entree='beef', drink='coffee')
# ? entree beef
# ? drink coffee


def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}

menu(**d)
# ?entree beef
# ? drink ice coffee
# ? dessert ice

# ! 位置引数 タプル化　キーワードを同時に扱う。


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

# ? banana
# ? ('apple', 'orange')
# ? {'entree': 'beef', 'drink': 'coffee'}
# pythonが引数を認識して、処理を行ってくれるが、順番が入れ替えできない。
