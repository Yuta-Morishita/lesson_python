# ! 数学関数を使ってみる

import math  # mathというpythonのライブラリーを呼び出しています

result = math.sqrt(25)  # math.sqrtでmathのライブラリーからsqrt関数を呼び出す。 sqrtは平方根の意味がある。
print(result)
# ? 出力結果 5

result2 = math.log2(10)
print(result2)
# ? 出力結果　

# pythonには数学の関数が準備されている
# mathをimportして利用できるので、関数を準備する必要がない。

print(help(math))
# 上記のようにhelp(math)を利用することで
# ドキュメントを表示させることができる。
