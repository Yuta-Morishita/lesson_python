
# ! zip関数

days = ['Mon', 'Tue', 'Wen']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])
# ? Mon apple coffee
# ? Tue banana tea
# ? Wen orange beer
# zip関数を使うとより綺麗に書ける

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
# ? Mon apple coffee
# ? Tue banana tea
# ? Wen orange beer
