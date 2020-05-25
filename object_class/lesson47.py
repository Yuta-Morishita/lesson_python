
# ! プロパティを使った属性の設定。


class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


baby = Baby()
adult = Adult()


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


car = Car()
car.ride(baby)


class ToyotaCar(Car):  # 継承することで、Carのメソッドを使用すること出来る。
    def run(self):
        print('fast')


class TeslaCar(Car):  # 独自の関数を適宜することも出来る。
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run  # enable_auto_runのFalseを書き換えられないうにしている。

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar('Model S')
print(tesla_car.enable_auto_run)
