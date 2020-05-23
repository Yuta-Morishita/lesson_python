
# ! 関数内で関数を使う。


def outer(a, b):

    def plus(c, d):  # outer関数から入ってきた、1,2の数字がc,dに入る。
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1+r2)


outer(1, 2)
# 関数の中で、繰り返すplusを使う時などに、インナー関数を使えばよい。
