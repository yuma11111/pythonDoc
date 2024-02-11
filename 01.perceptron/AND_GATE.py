#配列での計算などを行うことができる外部ライブラリ
import numpy as np

#パーセプトロン
#ANDゲートの実装
#def AND(x1, x2):
#
#    #
#    w1, w2, theta = 0.5, 0.5, 0.7
#    tmp = x1 * w1 + x2 * w2
#
#    #重みの総和が閾値を超えた場合に1を返す
#    if tmp <= theta:
#        return 0
#    elif tmp > theta:
#        return 1
#
#ANDゲートの動作確認
#print(AND(0, 0))
#print(AND(1, 0))
#print(AND(0, 1))
#print(AND(1, 1))

#ANDゲートを別の形式で実装
#import 
def AND(x1, x2):

    #入力値
    x = np.array([x1, x2])

    #重み
    w = np.array([0.5, 0.5])

    #バイアス（閾値）
    b = -0.7

    #重みの総和を算出し、バイアスを引く
    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

#ANDゲートの動作確認
#print(AND(0, 0))
#print(AND(1, 0))
#print(AND(0, 1))
#print(AND(1, 1))

#↑上記の2関数の動作は同じになることを確認