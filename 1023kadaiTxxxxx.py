#あるクラスの国語テストの変数
points_ja = [88, 76, 67, 43, 79, 80, 91]
sum_ja = sum(points_ja)
ave_ja = sum_ja / len(points_ja)
print("合計点は", sum_ja, "点")
print("平均点は", ave_ja, "点")

points_ma = [68, 76, 67, 43, 79, 80, 91]
sum_ma = 0
for i in points_ma:
    sum_ma += i
ave_ma = sum_ma / len(points_ma)
print("合計点は", sum_ma, "点")
print("平均点は", ave_ma, "点")

year = 2012
if year % 4 == 0:
    print("うるう年です")
elif year % 100 == 0:
    print("うるう年です")\
elif year % 400 == 0:
    print("うるう年です")
else:
    print("うるう年ではありません")
