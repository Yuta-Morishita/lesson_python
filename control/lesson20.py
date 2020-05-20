
# ! inとnotの学習　使いどころ

y = [1, 2, 3]
x = 1
if x in y:  # yにxは入っていますか？
    print('in')
    # ? in


if 100 not in y:  # 100がyの中に入っていませんか？
    print('not in')
    # ? not in

# ! notの使いどころ
is_ok = True

if is_ok:
    print('ok')
    # ? ok

if not is_ok:
    # boolen型を否定する。
    print('no')  # 出力されない
