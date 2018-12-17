# coding:utf-8
# elseを使って素数のケースでも結果を表示する
a_num = 59            # 素数かどうかを調べる数
for num in range(2, a_num):  # 2からa_num-1まで繰り返す
    if a_num % num == 0:     # a_numをnumで割り切れるか
        print(a_num, "は素数ではありません")
        break
else:
    # break文を一度も通らないでループが終了した
    print(a_num, "は素数です")
    # coding:utf-8
energy = 10
while energy > 0:
    print("走る")
    print("エネルギー:", energy)
    energy -=1;
print("エネルギーゼロ！")
