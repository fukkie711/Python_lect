#coding: UTF-8
# 課題
#教科書p133上のコードを写経
pref_capitals = {
(43.06417, 141.34694): "北海道(札幌)",
(40.82444, 140.74): "青森県(青森市)",
(39.70361, 141.1525): "岩手県(盛岡市)"
}
# 教科書p133下のコードを写経

loc = (39.70361, 141.1525)
for key in pref_capitals:
    if loc == key:
        print(pref_capitals[key])
        break

# 教科書p134のコードを写経
loc = (41.768793, 140.72881)  # 調べたい地点の緯度，経度
nearest_cap = ''              # 最寄りの県庁所在地名を保存する変数
nearest_dist = 10000          # 最寄りの地点までの距離を保存する変数
for key in pref_capitals:     # キーでループ
    # 緯度経度の差を二乗して距離を計算
    dist = (loc[0]-key[0])**2+(loc[1]-key[1])**2
    if nearest_dist > dist:
        # より近い地点が見つかったので，変数を入れ替え
        nearest_dist = dist
        nearest_cap = pref_capitals[key]

print(nearest_cap)
