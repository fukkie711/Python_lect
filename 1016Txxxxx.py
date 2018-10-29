lylic2 = "ずっと笑顔ばかりを選んで"
lylic2 += "泣き顔見せるのを迷ってた"
print(lylic2)

day = 24
str_day = str(day)
date = str_day + "日"
print(date)

tokyo_temps = [15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
print(tokyo_temps)
print(tokyo_temps[0])
print(tokyo_temps[5]-tokyo_temps[0])
print(tokyo_temps[-1]-tokyo_temps[0])
e_tokyo_temps = [13.6, 13.5, 14.2, 14.8, 14.8]
tokyo_temps2 = e_tokyo_temps + tokyo_temps
print(tokyo_temps2)

mcz = ["れに", "あかり", "かなこ", "しおり", "あやか", "ゆきな"]
print(mcz)
mcz[5] = "ももか"
print(mcz)

del mcz[0]
print(mcz)

momotamai = mcz[1:3]
print(momotamai)

print(mcz[:2])
print(mcz[1:])

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
plt.show()
