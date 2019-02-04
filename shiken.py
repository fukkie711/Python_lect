#1行コメントを書く
"""
複数行の
コメント
"""
#print()関数
print(5 - 5 + 1 + 9)
#数値を使った四則演算
kekka = (5 / 5 * (1 + 9))
# 5を2で割った余りの計算
print(5 % 2)
# 文字列を変数に代入
mojiretsu = "文字列"
# 文字列の連結
renketsu = "あいう"
renketsu = renketsu + "えお"
# 複合演算子を用いた文字列の連結
renketsu2 = "かきく"
renketsu2 =+ "けこ"
# 型変換
day = 24
str_day = str(day)
#リスト
tokyo_temps = [15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
#リストのうち，15.4を取り出す
print(tokyo_temps[1])
#リスト要素の置き換え あやかをももかに
mcz = ["れに", "あかり", "かなこ", "しおり", "あやか", "ゆきな"]
mcz[5] = "ももか"
#リスト要素の削除
del mcz[0]
#リストのスライス
mcz2 = ["れに", "あかり", "かなこ", "しおり", "あやか", "ももか"]
momotamai = mcz2[1:3] #注意：リストの1番目と2番めだけをスライスしている
#2次元配列
city_temps = [
[14.8, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9],
[10.0, 10.4, 11.5, 11.2, 10.9, 10.6, 11.8, 12.2],
[16.0, 15.5, 16.4, 15.9, 15.6, 15.6, 17.5, 17.1]
]
#2次元配列の要素取り出し
print(city_temps[1]) # 2行目（10.0, 10.4 ..., 12.2）を表示する
print(city_temps[2][0]) # 3行目1項目目(16.0)を表示する
#リストの合計，最大，最小
monk_fish_team = [158, 157, 163, 157, 145]
#リストの合計
print(sum(monk_fish_team))
#リストの最大
print(max(monk_fish_team))
#リストの最小
print(min(monk_fish_team))
#for文
mcz = ["れに", "かなこ", "しおり", "あやか", "ももか"]
for member in mcz:
    print(member)
#range()関数
for cnt in range(10):
    print(cnt)
#if文
#elifとelse
year = 2012
# うるう年の計算．
# 計算ロジックは
if year % 4 == 0:
    print("うるう年です")
elif year % 100 == 0:
    print("うるう年です")
elif year % 400 == 0:
    print("うるう年です")
else:
    print("うるう年ではありません")

# 関数の定義および引数の使用
def destiny_tank(num):
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    idx = num
    print("今日あなたが乗るべき幸運の戦車は", tanks[idx] , "です")
destiny_tank(2)
#関数の戻り値
def destiny_tank2(num):
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    idx = num
    return tanks[idx]
num = 1
tank = destiny_tank2(num)
print("今日あなたが乗るべき幸運の戦車は", tank , "です")

#モジュールを使う
# randomモジュールのインポート
import random
print(random.random())
print(random.randint(0, 6))
# asを使ったimport文の記法
import random as ra
print(ra.random())
print(ra.randint(0, 6))
# fromをつかったインポート
from random import random
print(random())
print(randint(0, 6))

#辞書型（ディクショナリ）
purple = {"ニックネーム": "れにちゃん", "出身地": "神奈川県", "キャッチフレーズ": "感電少女"}
print(purple["出身地"])
#ディクショナリのキーを使ったループ
purple = {"ニックネーム": "れにちゃん",
"出身地": "神奈川県",
"キャッチフレーズ": "感電少女",
"生年月日":"1993年6月21日"}
for key in purple:
    print(key, purple[key])

#リスト・タプル・集合型の特徴を覚えておくこと！
#リスト(list)：複数の値を持つことができる，生成方法：[0, 1, 2]
#set(集合型)：要素を重複できないリスト，生成方法：{0, 1, 2}
#タプル(tuple)：要素を変更できないタプル，生成方法：(0, 1, 2)

#whle文でループを作る
# whileを使ってfizzbuzz問題を解く
cnt = 1 # ループカウンタを初期化
while cnt <= 100: # 1から100まで繰り返し
    if cnt%3 == 0 and cnt%5 == 0: # 3で割り切れ，かつ5でも割り切れる
        print("FizzBuzz")
    elif cnt%3 == 0: # 3で割り切れる
        print("Fizz")
    elif cnt%5 == 0: # 5で割り切れる
        print("Buzz")
    else:
        print(cnt) # 数値を表示する
    cnt = cnt+1 # カウンタを1増やす

# break文とcontinue文を使ったループの制御
# ループブロック内で使える機能として、break文とcontinue分がある。どちらもループの流れを変える目的で利用する。
# break文は、ループに限らずブロックから抜け出すために使う。特別な条件でループを終えたいときに使うと便利
# continue文を使うと、それ以降のループブロックを実行せず、ブロックの最初まで戻ることができる。特定の条件にあるとき、ブロックの一部を実行せず、ループを抜けたいときに使うと便利

# 引数を特にしていないときに暗黙に指定される引数のことをデフォルト引数と呼ぶ
# 省略時に引数に渡される値をデフォルト値と呼ぶ

# 円とドルを変換する関数convert_currency(price, currency)を定義
def convert_currency(price, currency="円をドルに"):
    if currency == "円をドルに":
        result = price * 0.0088
    elif currency == "ドルを円に":
        result = price * 113.02
    print("為替は：", currency)
    print("元の値段は：", price)
    print("価格は：", result)
# convert_currency(price, currency)を読み出す。ただし、第一引数に10000を代入
convert_currency(10000)
# convert_currency(price, currency)を読み出す。ただし、引数のデフォルト値をかえる。currencyに"ドルを円に"を代入、priceに100を代入
convert_currency(currency="ドルを円に", price=100)

# 今日では、プログラムで大量のデータを扱うようになっている
# 複雑で規模の大きなプログラムを、より手軽に作ることが要求される
# そこで考案されたのがオブジェクト指向
# 命令型プログラミングではデータはデータ、命令は命令と別々に扱う
# データと命令を一緒にしてしまおう、というのがオブジェクト指向の基本的な考え方
# データと命令（メソッド）が一緒になっているもののことをオブジェクトと呼ぶ

# sort()メソッドを使ったリストのソート
# 昇順に並べ替える
monk_fish_team = [158, 157, 163, 157, 145]
monk_fish_team.sort()          # ソートをする

### Webアプリ編 ###
#第13回〜15回演習の「Webアプリ編」の「Webアプリの仕組み」のスライドは覚えておくこと！





### データ分析編 ###
# 最先端の機械学習アルゴリズムは何か？（モジュール名を答える）
# Pythonの科学技術計算向けグラフ描画ライブラリは何か？（モジュール名を答える）
