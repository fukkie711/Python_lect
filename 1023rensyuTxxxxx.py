city_temps = [
[14.8, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9],
[10.0, 10.4, 11.5, 11.2, 10.9, 10.6, 11.8, 12.2],
[16.0, 15.5, 16.4, 15.9, 15.6, 15.6, 17.5, 17.1]
]
print(city_temps)
print(city_temps[1])
print(city_temps[2][7]- city_temps[2][0])

import matplotlib.pyplot as plt
plt.plot(city_temps[0])
plt.plot(city_temps[1])
plt.plot(city_temps[2])
# plt.show()

monk_fish_team = [158, 157, 163, 157, 145]
print(sum(monk_fish_team))
print(max(monk_fish_team))
print(min(monk_fish_team))
# 応用編 平均の計算
monk_mean = sum(monk_fish_team) / len(monk_fish_team)
print(monk_mean)

plt.bar([0, 1, 2, 3, 4], monk_fish_team)
# plt.show()
# plt.plot([0, len(monk_fish_team)], [monk_mean, monk_mean], color = 'red')

mcz = ["れに", "かなこ", "しおり", "あやか", "ももか"]
for member in mcz:
    print(member)

for cnt in range(10):
    print(cnt)

if 1 == 1:
    print("1True")
if 5**(4-4)+9 == 10:
    print("2True")
if 2 < len([0, 1, 2]):
    print("3True")
if sum([1, 2, 3, 4]) < 10:
    print("4True")

if "AUG" == "AUG":
    print("1True")
if "AUG" == "aug":
    print("2True")
if "あいう" == "あいう":
    print("3True")

if "GAG" in "AUGACGGAGCUU":
    print("1True")
if "恋と戦いはあらゆることが正当化されるのよ" in "正当化":
    print("2True")
if "stumble" in "A hourse may stumble though he has four legs":
    print("3True")

if [1, 2, 3, 4] == [1, 2, 3, 4]:
    print("1True")
if [1, 2, 3] == [2, 3]:
    print("2True")
if [1, 2, 3] == ['1', '2', '3']:
    print("3True")

if 2 in [2, 3, 5, 7, 11]:
    print("1True")
if 21 in [13, 17, 19, 23, 29]:
    print("2True")
if 'アッサム' in ['ダージリン', 'アッサム', 'オレンジペコ']:
    print("3True")

if 2^3-2+4 == 10:
    print("式1は10")
else:
    print("式1は10にならない")
if 2**3-2+4 == 10:
    print("式2は10になる")
else:
    print("式2は10にならない")

a_year = 2080
if a_year >= 1993:
    if a_year == 1993:
        print(a_year, "年、れに誕生")
    else:
        print(a_year, "年、れに", a_year - 1993, "歳")

a_num = 57
for num in range(2, a_num):
    if a_num % num == 0:
        print(a_num, "は素数ではありません")
        break
