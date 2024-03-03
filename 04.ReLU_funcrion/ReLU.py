#ReLUは「Rectified Linear Unit」の略
#入力が0を超えていればその入力をそのまま出力
#入力が0以下なら0を出力する関数

import numpy as np
import matplotlib.pylab as plt

def Relu(x) :
    return np.maximum(0, x) #入力された値のうち大きい方を返す関数

x = np.arange(-1.0, 1.0, 0.1)
y = Relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

#0までは0の出力が続き、0を超えたタイミングから斜めに上がっていく直線を描く
