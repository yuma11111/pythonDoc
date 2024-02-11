#
# NAND（NOT AND）ゲートの実装と動作確認
#

#配列での計算などを行うことができる外部ライブラリ
import numpy as np

#NANDゲートの実装
#ANDゲートとの違いは、重みとバイアスの正負のみ
def NAND(x1, x2):

    #入力値
    x = np.array([x1, x2])

    #重み
    w = np.array([-0.5, -0.5])

    #バイアス（閾値）
    b = 0.7

    #重みの総和を算出し、バイアスを引く
    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

#NANDゲートの動作確認
#print(NAND(0, 0))
#print(NAND(1, 0))
#print(NAND(0, 1))
#print(NAND(1, 1))

#動作確認を行い、ANDゲートと逆の結果となることを確認した。