
# ! 文字列を代入してみる。
# ! .formatを使って{}に代入すると、文字列型に変換される

a = 'Mike is {}'.format('kind')
print(a)
# ? 実行結果 Mike is kind
# .format('')とすることで
# ''の中の文字列を{}の中に代入することができる。

b = 'Mike is {},{},{}'.format('kind', 'busy', 'cheerful')
print(b)
# ? 実行結果　Mike is kind,busy,cheerful
# {}を複数準備することも出来る。

c = 'Mike is {2},{1},{0}'.format('kind', 'busy', 'cheerful')
print(c)
# ? 実行結果 Mike is cheerful,busy,kind
# {}の中に番号を振ると.format()の中のインデックスの順番通りに表示できる。

d = 'My name is {name} {family}.Watashi ha {family} {name} desu'.format(name='Jun', family='Sakai')
print(d)
# ? 実行結果 My name is Jun Sakai.Watashi ha Sakai Jun desu
# {}の中に変数を使うことができる。実行結果のように変数が代入される。
