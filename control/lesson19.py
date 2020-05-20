
# ! if文の作成

x = -10

if x < 0:
    print('negative')
    # ? negative
else:
    print('positive')


x = 10

if x < 0:
    print('negative')
else:
    print('positive')
    # ? positive

x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')
    # ? zero


x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:  # elifは複数作成が可能
    print('10')
else:
    print('positive')
    # ? 10

# ! if分の注意点

x = 10

if x < 0:
    print('negative')
elif x == 10:
    print('zero')  # if文は上から順に呼び込まれる。
elif x == 10:
    print('10')
else:
    print('positive')
    # ? zero

# ! if文の中にif文を作成する。

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
        # ? a is positive
        # ? b is positive

if a < 0:
    print('a is positive')  # このif文がTrueでなければ、下のif文は呼び出されない。
    if b > 0:
        print('b is positive')
        # ? a is positive
        # ? b is positive
