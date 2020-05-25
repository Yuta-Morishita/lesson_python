
# ! クラスの変数


class Person(object):

    def __init__(self, name):
        self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()
# ? A human
# ? B human


class Person(object):

    kind = 'human'  # クラス変数を宣言する。 宣言されたクラス変数は、オブジェクトの中で共有される。

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()
# ? A human
# ? B human


class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)
# ? ['add 1', 'add 2']
