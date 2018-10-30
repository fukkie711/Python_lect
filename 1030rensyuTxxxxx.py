# リストの値の合計（for文を使う）
the_list = [101, 123, 152, 123]
summary = 0
for item in the_list:
    summary = summary + item
print(summary)

# リストの値の合計（関数を使う）
the_list = [101, 123, 152, 123]
summary2 = sum(the_list)
print(summary2)

#絶対値を計算
print(abs(10))
print(abs(-20))

#
print(int("100"))
print(int("100", 2)) #2進数の100は1×2の2乗になるので4
print(int("100", 16)) #16進数の100は1×16の2乗になるので256

def destiny_tank():
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    num = input("好きな数字を入力してください：")
    idx = int(num) % len(tanks)
    print("あなたの運命の戦車は")
    print(tanks[idx])

def destiny_tank2(num):
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    idx = num % len(tanks)
#    print("あなたの運命の戦車は")
    print(tanks[idx])

destiny_tank2(2)

def destiny_tank3(num):
    tanks = ["No IV typeD", "No III typeJ", "Churchill Mk.VII", "M4 sharman", "P40", "T-34/76"]
    idx = num % len(tanks)
    return tanks[idx]

from random import randint
num = randint(0, 10)
tank = destiny_tank3(num)
#print("今日あなたが乗るべき幸運の戦車は", tank, "です")

import random

print(random.random())
print(random.randint(0, 6))
a_list = [0, 1, 2, 3, 4, 5]
random.shuffle(a_list)
print(a_list)
print(random.choice(a_list))
