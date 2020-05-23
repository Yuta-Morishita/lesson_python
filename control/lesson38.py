
# ! クロージャーの学習


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area  # これまではここで関数を実行するためのcircle_area()を行っていた。


cal1 = circle_area_func(3)
cal2 = circle_area_func(3.14)

# 半径１０を代入
print(cal1(10))  # ここで実行されている。
print(cal2(10))  # ここで実行されている。
# ? 300
# ? 314.0

# 選択肢を与える際などに、有効である。
