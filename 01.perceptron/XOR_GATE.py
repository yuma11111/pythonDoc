#
# NAND（NOT AND）ゲートの実装と動作確認
#

#配列での計算などを行うことができる外部ライブラリ
import numpy as np

#これまで作成したゲート作成関数を呼び出す
import AND_GATE as modAnd
import NAND_GATE as modNand
import OR_GATE as modOr

#NANDゲートの実装
#ANDゲートとの違いは、重みとバイアスの正負のみ
def XOR(x1, x2):

    #NANDゲートに渡す
    s1 = modNand.NAND(x1, x2)

    #ORゲートに渡す
    s2 = modOr.OR(x1, x2)

    #NANDゲートとORゲートの返り値をANDゲートに渡す
    return modAnd.AND(s1, s2)

#NANDゲートの動作確認
print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))

#動作確認を行い、書籍に記載されているものと同様に