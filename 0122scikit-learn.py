#scikit learn のサンプル学習データを取り込む
from sklearn import datasets

# 描画のためにmatplotlibモジュールを取り込む
from matplotlib import pyplot as plt, cm

# 手書き数字データを読み込む
digits = datasets.load_digits()
data = digits.images[0]

# 描画
plt.imshow(data.reshape(8, 8), cmap=cm.gray_r, interpolation='nearest')
plt.show()

from sklearn import datasets, model_selection, svm, metrics

# 手書き数字データを読み込む
digits = datasets.load_digits()

# 訓練用データとテスト用データに分ける
data_train, data_test, label_train, label_test = model_selection.train_test_split(digits.data, digits.target)

# SVMアルゴリズムを利用してモデルを構築する
clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)

# テストデータでの分類結果を予測してみる
predict = clf.predict(data_test)

# 結果を表示する/
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("分類期の情報＝", clf)
print("正解率＝", ac_score)
print("レポート＝\n", cl_report)
