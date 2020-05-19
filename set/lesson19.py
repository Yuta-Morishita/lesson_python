
# ! 集合の使い方

# 共通の友人を探すなど、共通の何かを見つける時に使える。

my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)  # 共通の友人を取り出す。
# ? {'B'}


# リストのデータからユニークな値だけを取り出した時に使用できる。

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
# ? {'apple', 'banana'}
