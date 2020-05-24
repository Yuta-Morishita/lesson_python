
l = []  # 空の配列を用意する。


def math(l):  # mathの関数に、空のリストを引数で渡す。
    n = 1
    while n < 81:
        a = n ** 4
        l.append(a)  # 計算されたaを配列に追加する。
        # ? [1,16,81]と順番に配列に数字が入る。
        n += 1
    return l


r = math(l)  # 関数を呼び出す。
print(sum(r))
# ? 676010664
