
# ! クラスの定義


class Person(object):
    def __init__(self, name):  # 一番初めに呼ばれる
        self.name = name
        print(self.name)

    def say_something(self):  # self で代入されたMikeが引数
        print('I am {}.hello'.format(self.name))
        self.run()

    def run(self):
        print('run')

    def __del__(self):  # person.say_something()が必要ないとなれば使われる関数。
        print('good bye')


person = Person('Mike')
person.say_something()
del person

print('@@@@')
