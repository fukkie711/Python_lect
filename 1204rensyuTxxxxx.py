# coding:utf-8
# 地球上から水平に打ち出した物体が速度(v)によって
# どのような振る舞いをするかを調べる
v = 30000
if v < 28400:
    print("地上に落下します")
if v >= 28400 and v < 40300:
    print("月とお友達です")
if v >= 40300 and v < 60100:
    print("惑星の仲間入りです")
if v >= 60100:
    print("アルファケンタウリを目指せ")

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

# じゃんけんプログラム
from random import randint              # 乱数を作る関数を読み込む
hands = {0:"グー", 1:"チョキ", 2:"パー"}  # じゃんけんの手
# 勝ち負けのルール
rules = {(0, 0):"あいこ", (0, 1):"勝ち",   (0, 2):"負け",
         (1, 0):"負け",   (1, 1):"あいこ", (1, 2):"勝ち",
         (2, 0):"勝ち",   (2, 1):"負け",   (2, 2):"あいこ"}

while True:
    # じゃんけんのループ
    pc_hand = randint(0, 2)             # 乱数で手を決める
    user_hand_str = input("0:グー 1:チョキ 2:パー 3:やめる")
    #user_hand_str = "3"
    if user_hand_str == "3":
        # 終了の数値が入力されたので，ループを抜ける
        break
    if user_hand_str not in ("0", "1", "2"):
        # 不正な入力の場合，ループの先頭に戻る
        continue
    user_hand = int(user_hand_str)     # ユーザの手を数値に変換
    # 手を表示する
    print("あなた"+hands[user_hand]+"，コンピュータ:"+hands[pc_hand])
    # 勝ち負けを表示する
    print(rules[(user_hand, pc_hand)])

# elseを使って素数のケースでも結果を表示する
a_num = 59            # 素数かどうかを調べる数
for num in range(2, a_num):  # 2からa_num-1まで繰り返す
    if a_num % num == 0:     # a_numをnumで割り切れるか
        print(a_num, "は素数ではありません")
        break
else:
    # break文を一度も通らないでループが終了した
    print(a_num, "は素数です")
