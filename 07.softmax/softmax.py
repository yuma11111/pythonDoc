import numpy as np

def softmax_(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

#指数が使われる関係上計算結果がとても大きくなる
#その影響で計算結果が不安定になるらしい。
#それを改善したバージョン↓
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #ここがオーバーフロー対策らしい
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)

#出力結果：[0.01821127 0.24519181 0.73659691]
#ソフトマックス関数の出力は0から1.0の間の実数となる
print(y)

#出力結果の総和は1.0となる。
print(np.sum(y))

#ソフトマックス関数の出力を確率として解釈することができる