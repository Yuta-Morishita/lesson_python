
# ! クラスの継承

# class Carが持っているオブジェクトの機能を、ToyotaCarに継承をする。


class Car(object):
    def run(self):
        print('run')


class ToyotaCar(Car):  # 継承することで、Carのメソッドを使用すること出来る。
    pass


class TeslaCar(Car):  # 独自の関数を適宜することも出来る。
    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
