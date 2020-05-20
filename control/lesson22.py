
# ! Noneの判定を行う。

is_empty = None  # 変数は宣言するが、何も入れたくない時にNoneを宣言する。
print(is_empty)
# ? None

if is_empty == None:  # pythonでは勧められた書き方ではない。
    print('None!!!')
    # ? None!!!

if is_empty is None:
    print('None!!!')
    # ? None!!!

# ! isとは何か？

print(1 == True)
# ? True

print(1 is True)
# ? False
# オブジェクト同士が同じであると認識しなければ、Trueを返さない。
