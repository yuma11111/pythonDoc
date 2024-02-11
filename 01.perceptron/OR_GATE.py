#
# ORゲートの実装と動作確認
#

#配列での計算などを行うことができる外部ライブラリ
import numpy as np

#NANDゲートの実装
#ANDゲートとの違いは、重みとバイアスの正負のみ
def OR(x1, x2):

    #入力値
    x = np.array([x1, x2])

    #重み
    w = np.array([0.5, 0.5])

    #バイアス（閾値）
    b = -0.2

    #重みの総和を算出し、バイアスを引く
    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

#NANDゲートの動作確認
#print(OR(0, 0))
#print(OR(1, 0))
#print(OR(0, 1))
#print(OR(1, 1))

#動作確認を行い、閾値を超えた場合のみ1を返却することを確認した。

#次にorゲートを視覚的に表現する
#import matplotlib.pyplot as plt

#実行結果を格納した配列
#x = np.array([OR(0, 0), OR(1, 0), OR(0, 1), OR(1, 1)])
#y = np.sin(x)

#plt.plot(x, y)

#書籍とは同じにならないが、とりあえず描画してみる
#plt.show()