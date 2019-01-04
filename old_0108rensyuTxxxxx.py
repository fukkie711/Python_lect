#coding: UTF-8
import numpy as np
reactions_in_ms = np.loadtxt('/Users/k-fukuzawa/Dropbox/01_AIT/2018/01_非常勤/04_プログラミング及び演習1/Python_lect/reactions.txt')

print(reactions_in_ms.size)
print(reactions_in_ms[:20])

reactions_in_sec = reactions_in_ms / 1000
print(reactions_in_sec[:20])

print("平均値：", np.mean(reactions_in_sec))
print("中央値：", np.median(reactions_in_sec))
print("標準偏差：", np.std(reactions_in_sec))
print("最小値：", np.min(reactions_in_sec))
print("最大値：", np.max(reactions_in_sec))

import pandas as pd
reactions_df = pd.DataFrame(reactions_in_sec)
print(reactions_df.head())
print(reactions_df.describe())

%matplotlib inline
import matplotlib.pyplot as plt
h = plt.hist(reactions_in_sec)

import numpy as np
a = np.array([0, 1, 2, 3])
a

b = np.array([[0,0,0],[0,0,0],[0,0,0]])
b
print(b.ndim) #次元数
print(b.shape) #各次元の要素数
print(b.size) #サイズ
print(b.dtype) #型

#2次元配列に変換する
b2 = np.zeros(9).reshape(3,3)
b2
a = np.arange(9).reshape(3,3)
a

#90度回転したarrayを表示
a.T

#1から9までの配列を作る
a = np.arange(1, 10)
a
#各要素に1を足して表示
a+1

#1から9までの配列を2つ作る
a = np.arange(1, 10)
b = np.arange(1, 10)
a+b


import numpy as np
import matplotlib.pyplot as plt
s = np.sin(np.pi*np.arange(0.0, 2.0, 0.01))
t = plt.plot(s)

x = np.random.randn(5000)
y = np.random.randn(5000)
t = plt.plot(x, y, 'o', alpha=0.1)

x = np.array([1.628, 3.363, 5.145, 7.683, 9.855])
y = np.array([1.257, 3.672, 5.841, 7.951, 9.775])
a = np.array([x, np.ones(x.size)])
a = a.T
m, c = np.linalg.lstsq(a, y, rcond=None)[0]
t = plt.plot(x, y, 'o')
t = plt.plot(x, (m*x+c))

import numpy as np

#乱数のシードを設定
np.random.seed(9)
# 0から1まで100個の数値を作成、乱数要素を混ぜる前のx
x_orig = np.linspace(0, 1, 100)

def f(x):
    # xに対応するsinを返す関数
    return np.sin(2 * np.pi * x)

# 0から1まで100個のバラけたサンプルデータ(x)を作成
x = np.random.uniform(0, 1, size=100)[:, np.newaxis]
# xに対応するsinに乱数を足してサンプルデータ(y)を作成
y = f(x)+np.random.normal(scale=0.3, size=100)[:, np.newaxis]

#グラフの作成
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 学習用データとテスト用データに分ける
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8)

# 元のsinとサンプルデータをplot
plt.plot(x_orig, f(x_orig), ls=':')
plt.scatter(x_train, y_train)
plt.xlim((0,1))
# import math
# import numpy as np
# from matplotlib import pyplot
#
# print('goodbye')
# pi = math.pi
# x = np.linspace(0, 2*pi, 100)
# y = np.sin(x)
#
# pyplot.plot(x, y)
# pyplot.show()
#
# x = np.linspace(0, 3*np.pi, 500)
# plt.plot(x, np.cos(x**2))
# plt.show()
#
# import numpy as np
# reactions_in_sec = np.loadtxt('reactions.txt')
# import matplotlib.pyplot as plt
# h = plt.hist(reactions_in_sec)
# #plt.show()
#
# np.random.seed(9)
#
# x_orig = np.linspace(0, 1, 100)
#
# def f(x):
#     return np.sin(2 * np.pi * x)
#
# x = np.random.uniform(0, 1, size=100)[:, np.newaxis]
#
# y = f(x)+np.random.normal(scale=0.3, size=100)[:, np.newaxis]
#
# from sklearn.model_selection import train_test_split
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8)
#
# plt.plot(x_orig, f(x_orig), ls=':')
# plt.scatter(x_train, y_train)
# plt.xlim((0,1))
