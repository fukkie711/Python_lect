# coding:utf-8
# リスト要素のインデックスを探す関数
def find_index(the_list, target):
    # the_listからtargetのインデックスを調べる関数
    idx = 0            # インデックス用のカウンタを初期化
    for item in the_list:   # リストの要素を一つずつ調べる
        if target == the_list[idx]:
            # 調べたい要素が見つかったのでインデックスを返す
            return idx
        idx = idx+1    # インデックスを1増やす
# リストを定義
mcz=["れに", "かなこ", "しおり", "あやか", "ももか"]
print(find_index(mcz, "しおり"))

# メソッドを使って同じ処理を書く方が簡単
print(mcz.index("しおり"))

# 文字列の置換と削除
# 置換前の文字列を定義
orig_str = "いっぱい"
# 文字列の「い」を「お」に置換、結果を表示
print(orig_str.replace("い", "お")  )

# カンマ付き文字列の削除と数値への変換
# カンマの入った整数相当の文字列
str_num = "1,000,000"
print(str_num)
# カンマを取り除きint()で数値にする
num = int(str_num.replace(",", ""))
print(num)

# splitメソッドの使用例
import matplotlib.pyplot as plt

str_speeds = "38 42 20 40 39"       # 戦車のスピード(km/h)
str_armor = "80 50 17 50 51"        # 戦車の装甲厚(mm)
speeds = str_speeds.split(" ")      # 速度をスペースで分割
armors = str_armor.split(" ")       # 装甲厚をスペースで分割
markers = ["o", "v", "^", "<", ">"]

for idx in range(len(speeds)):      # リストの長さ分ループ
    x = int(speeds[idx])            # 文字列を数値に変換
    y = int(armors[idx])
    # 散布図を描く
    plt.scatter(x, y, marker=markers[idx])
plt.show()
#IV号戦車(o) LT-38(v) 八九式中戦車(^) III号突撃砲(<) M3中戦車(>)

# split()した文字列をjoin()で連結
str_speeds = "38 42 20 40 39"  # 空白で区切られた数値
speeds = str_speeds.split()    # 空白で分割
csep_speeds = ",".join(speeds) # コンマで連結
print(csep_speeds)             # 結果を表示

# エスケープシーケンスを使って改行文字を入れるとすっきりする
def func():
    words = "ゆく河の流れは絶えずして\nしかももとの水にあらず"
    print(words)

func()

# sort()メソッドを使ったリストのソート
# 昇順に並べ替える
monk_fish_team = [158, 157, 163, 157, 145]
monk_fish_team.sort()          # ソートをする
print(monk_fish_team)          # リストの内容を確認

# 降順に並べ替える
monk_fish_team.sort(reverse=True)  # ソートをする
print(monk_fish_team)              # リストの内容を確認
