# 下のやつを実行するのに必要
def destiny_tank2(num):
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    idx = num % len(tanks)
    print("あなたの運命の戦車は")
    print(tanks[idx])

# p.101のコード（ランダムな結果を戻す）
from random import randint
num = randint(0, 10)
destiny_tank2(num)

# p.102のコード（戻り値を持つ関数の定義）
def destiny_tank3(num):
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    idx = num % len(tanks)
    return tanks[idx]

# p.102のコード（destiny_tank3()関数の実行例）
from random import randint
num = randint(0, 10)
tank = destiny_tank3(num)
print("今日あなたが乗るべき幸運の戦車は", tank , "です")

# p.105の下のコード（calc_variance()関数の定義）
def calc_variance(a_list):
    total = sum(a_list)
    length = len(a_list)
    mean = total / length
    variance = 0

    for height in a_list:
        variance += (height - mean)**2
    variance = variance/len(a_list)

    return variance

# p.106のコード（calc_variance()関数の実行例）
monk_fish_team = [158, 157, 163, 157, 145]
volleyball_team = [143, 167, 170, 165]
pravda_team = [127, 172, 140, 160, 174]

monk_team_variance = calc_variance(monk_fish_team)
volley_team_variance = calc_variance(volleyball_team)
pravda_team_variance = calc_variance(pravda_team)

# 標準偏差の計算。0.5乗==1/2乗。つまり平方根（ルート）
print(monk_team_variance**0.5)
print(volley_team_variance**0.5)
print(pravda_team_variance**0.5)
