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
# 文字列を表示
print(mojiretsu)
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
print(mcz)
#リスト要素の削除
del mcz[0]
#リストのスライス
momotamai = mcz[1:3] #注意：リストの1番目と2番めだけをスライスしている
#スライスの記法（省略）
mcz2 = ["れに", "あかり", "かなこ", "しおり", "あやか", "ももか"]
print(mcz[:2])
print(mcz[1:])
#2次元配列
city_temps = [
[14.8, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9],
[10.0, 10.4, 11.5, 11.2, 10.9, 10.6, 11.8, 12.2],
[16.0, 15.5, 16.4, 15.9, 15.6, 15.6, 17.5, 17.1]
]
#2次元配列の要素取り出し
print(city_temps)
print(city_temps[1])
print(city_temps[2][0])
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
#値の変更
print(purple["キャッチフレーズ"])
purple["キャッチフレーズ"] = "鋼少女"
print(purple["キャッチフレーズ"])
#新しいキーと値を追加
purple["生年月日"] = "1993年6月21日"
print(purple["生年月日"])
#キーを使って要素を削除する
del purple["ニックネーム"]
#ディクショナリのキーを使ったループ
purple = {"ニックネーム": "れにちゃん",
"出身地": "神奈川県",
"キャッチフレーズ": "感電少女",
"生年月日":"1993年6月21日"}
for key in purple:
    print(key, purple[key])

#set
#setはどんなことに使うのか
#setは集合を扱うためにPythonに追加された
#setの定義
dice = {1, 2, 3, 4, 5, 6}
#setの和集合
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}
print(fib)
prime_fib = prime | fib
#setの差集合
dice = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6, 8, 10}
odd_dice = dice - even

"""
リスト・タプル・集合型の特徴を覚えておくこと！
リスト(list)：複数の値を持つことができる，生成方法：[0, 1, 2]
set(集合型)：要素を重複できないリスト，生成方法：{0, 1, 2}
タプル(tuple)：要素を変更できないタプル，生成方法：(0, 1, 2)
"""

#条件式に論理演算子(andやor)を使った例
v = 30000
if v < 28400:
    print("地上に落下します")
if v >= 28400 and v < 40300:
    print("月とお友達です")
if v >= 40300 and v < 60100:
    print("惑星の仲間入りです")
if v >= 60100:
    print("アルファケンタウリを目指せ")
#whle文でループを作る
# whileを使ってfizzbuzz問題を解く
cnt = 1         # ループカウンタを初期化
while cnt <= 100:         # 1から100まで繰り返し
    if cnt%3 == 0 and cnt%5 == 0:
        print("FizzBuzz") # 3で割り切れ，かつ5でも割り切れる
    elif cnt%3 == 0:
        print("Fizz")     # 3で割り切れる
    elif cnt%5 == 0:
        print("Buzz")     # 5で割り切れる
    else:
        print(cnt)        # 数値を表示する
    cnt = cnt+1           # カウンタを1増やす

"""
break文とcontinue文を使ったループの制御
ループブロック内で使える機能として、break文とcontinue分がある。どちらもループの流れを変える目的で利用する。
break文は、ループに限らずブロックから抜け出すために使う。特別な条件でループを終えたいときに使うと便利
continue文を使うと、それ以降のループブロックを実行せず、ブロックの最初まで戻ることができる。特定の条件にあるとき、ブロックの一部を実行せず、ループを抜けたいときに使うと便利
"""

"""

引数を特にしていないときに暗黙に指定される引数のことをデフォルト引数と呼ぶ
省略時に引数に渡される値をデフォルト値と呼ぶ
---問題---
# 円とドルを変換する関数convert_currency(price, currency)を定義し、円→ドルの計算とドル→円の計算をそれぞれ実行しなさい。
# 関数convert_currency(price, currency)のcurrencyのデフォルト値を"円をドルに"と指定
# もし、currencyが"円をドルに"だったら
# price に 0.0088をかけた値をresultに代入
# もし、currencyが"ドルを円に"だったら
# priceに113.02をかけた値をresultに代入
# ”為替は：” と表示してcurrencyを表示する
# ”元の値段は"と表示してpriceを表示する
# "価格は："と表示してresultを表示する
# convert_currency(price, currency)を読み出す。ただし、第一引数に10000を代入
# convert_currency(price, currency)を読み出す。ただし、引数のデフォルト値をかえる。currencyに"ドルを円に"を代入、priceに100を代入
---問題終了---
"""
# 上記の解答例--開始
def convert_currency(price, currency="円をドルに"):
    if currency == "円をドルに":
        result = price * 0.0088
    elif currency == "ドルを円に":
        result = price * 113.02
    print("為替は：", currency)
    print("元の値段は：", price)
    print("価格は：", result)
convert_currency(10000)
convert_currency(currency="ドルを円に", price=100)
# 解答例--終了

"""
今日では、プログラムで大量のデータを扱うようになっている
複雑で規模の大きなプログラムを、より手軽に作ることが要求される
そこで考案されたのがオブジェクト指向
命令型プログラミングではデータはデータ、命令は命令と別々に扱う
データと命令を一緒にしてしまおう、というのがオブジェクト指向の基本的な考え方
データと命令（メソッド）が一緒になっているもののことをオブジェクトと呼ぶ
≒データや命令をまとめてオブジェクトとして捉える手法＝オブジェクト指向
"""

# 文字列の置換と削除
# 置換前の文字列を定義
orig_str = "いっぱい"
# 文字列の「い」を「お」に置換、結果を表示
print(orig_str.replace("い", "お")  )

# sort()メソッドを使ったリストのソート
# 昇順に並べ替える
monk_fish_team = [158, 157, 163, 157, 145]
monk_fish_team.sort()          # ソートをする
print(monk_fish_team)          # リストの内容を確認
# 降順に並べ替える
monk_fish_team.sort(reverse=True)  # ソートをする
print(monk_fish_team)              # リストの内容を確認

### Webアプリ編 ###
#第13回〜15回演習の「Webアプリ編」の「Webアプリの仕組み」のスライドは覚えておくこと！
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
#ヘッダ情報を入力
print("Content-Type: text/html; charset=utf-8")
#ヘッダと本体データを区切る空行
print("")
#本体のデータを出力
#ランダムな数を取得
no = random.randint(1, 6)
#画面に出力
print("""
<html>
<head><title>サイコロ</title></head>
<body>
    <h1>{num}</h1>
</body></html>
""".format(num=no)) #p177のformat()メソッド

### データ分析編 ###
"""
Q.最先端の機械学習アルゴリズムは何か？（モジュール名を答える）
Q.Pythonの科学技術計算向けグラフ描画ライブラリは何か？（モジュール名を答える）
"""
