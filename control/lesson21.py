
# ! 値が入っているか判定する。

is_ok = True

if is_ok:
    print('OK!')
else:
    print('NO!')
    # ? OK!

is_ok = 1

if is_ok:
    print('OK!')
else:
    print('NO!')
    # ? OK!

is_ok = 0

if is_ok:
    print('OK!')
else:
    print('NO!')
    # ? NO!

# 変数の中身があれば、Trueを返す。

is_ok = ''  # 文字列が入っているかの判定。

if is_ok:
    print('OK!')
else:
    print('NO!')
    # ? NO!

