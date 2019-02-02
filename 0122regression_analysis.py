import numpy as np
### 下準備 ###
#乱数のシードを設定
np.random.seed(9)
# 0から1まで50個の数値を生成，乱数要素を混ぜる前のx
# x_orig = np.linspace(0, 1, 100)
x_orig = np.linspace(0, 35, 50)

def f(x):
    # xに対するsinを返す関数
    return np.sin(2 * np.pi * x)
def f2(x):
    # 気温とアイスクリームの本数の関係を返す関数(適当)
    return (2 / 5) * x + 2

# 0から30まで50個のバラけたサンプルデータ(x)を生成
# xに対応するy=f2(x)に乱数値を足してサンプルデータ(y)を生成
#標準偏差4くらいで適当にばらつかせてリアル感を出す
x = np.random.uniform(0, 30, size=50)[:, np.newaxis]
y = f2(x)+np.random.normal(scale=4, size=50)[:, np.newaxis]

# グラフの作成
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
### 終了_下準備 ###

### ここからがデータ分析 ###
# 学習用データとテスト用データに分ける
# データの8割をテストデータにする
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8)

# 元の値とサンプルデータをplot
plt.figure(figsize=(7, 5))
plt.scatter(x_train, y_train)
plt.xlim((0, 35))
plt.ylim((0, 30))
plt.xlabel('Tempreture')
plt.ylabel('Icecream')

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# 2x2のグラフを描く準備をする
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# 予測式 1, 2, 3, 7次式について学習した結果を表示
# for ax, deg in zip(axs.ravel(), [1, 2, 3, 7]):
for ax, deg in zip(axs.ravel(), [1, 3, 5, 7]):
    # パイプラインを作る
    e = make_pipeline(PolynomialFeatures(deg), LinearRegression())
    # 学習セットで学習をする
    e.fit(x_train, y_train)

    # 元のxを与えて予測
    px = e.predict(x_orig[:, np.newaxis])
    # 予測結果のグラフとテキストデータの点を描画
    ax.scatter(x_train, y_train)
    ax.plot(x_orig, px)
    ax.set(xlim=(0, 35), ylim=(0,30), ylabel='Icecream', xlabel='Tempreture', title='degree={}'.format(deg))

# plt.tight_layout
# plt.show()
