# coding:utf-8
dice = {1, 2, 3, 4, 5, 6}
coin = {"表", "裏"}

# 和集合を得る
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}

prime_fib = prime | fib
print(prime_fib)

# 差集合の作成
dice = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6, 8, 10}

odd_dice = dice - even
print(odd_dice)

prefs = {"北海道", "青森", "秋田", "岩手"}
capitals = {"札幌", "青森", "秋田", "盛岡"}

pref_cap = prefs & capitals
print(pref_cap)

pref_cap2 = prefs ^ capitals
print(pref_cap2)

codon = ['ATG', 'GGC', 'TCC', 'AAG', 'TTC', 'TGG', 'GAC', 'TCC']
s_codon = set(codon)
print(len(codon), len(s_codon))

# 要素の検索とsetの比較
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}
prime_fib = prime | fib

prime_fib = prime & fib # 2つの交わりを得る
if 13 in prime_fib:
    print("13は素数で、フィボナッチ数でもある")
if {2, 3} <= prime_fib: #部分集合かどうかを確かめている
    print("2, 3は素数で、フィボナッチ数でもある")

# タプルの定義
month_names = ("January", "February", "March", "April",
"May", "June", "July")

print(month_names[1])

# タプルは要素の変更ができない
# month_names[0] = "睦月"

# タプルの連結
month_names = month_names + ("August", "September", "October",
"November", "December")
print(month_names)
print(month_names[11])

#タプルをキーとしたディクショナリの作成
pref_capitals = {
(43.06417, 141.34694): "北海道(札幌)",
(40.82444, 140.74): "青森県(青森市)",
(39.70361, 141.1525): "岩手県(盛岡市)"
}

loc = (39.70361, 141.1525)
for key in pref_capitals:
    if loc == key:
        print(pref_capitals[key])
        break
