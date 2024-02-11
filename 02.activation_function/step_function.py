#配列同士の計算を行う
import numpy as np

#グラフの描写
import matplotlib.pylab as plt

#ステップ関数の実装
def step_function(x):

    #引数のxに配列だった場合、ブロードキャスト機能により
    #配列の要素数が一致するような形で認識される
    #「x > 0」のけっかはbooleanであるため、数値に変換する...はずだが、
    # なぜかエラーになるので、一旦下記の処理に変更中
    #return np.array(x > 0, dtype=np.int)
    return np.array(x > 0)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()