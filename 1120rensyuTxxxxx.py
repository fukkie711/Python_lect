#coding: UTF-8
purple = ["れにちゃん", "神奈川県", "感電少女"]

purple = {"ニックネーム": "れにちゃん",
"出身地": "神奈川県",
"キャッチフレーズ": "感電少女"}

print(purple["出身地"])
purple["キャッチフレーズ"] = "鋼少女"
print(purple["キャッチフレーズ"])

purple["生年月日"] = "1993年6月21日"
print(purple["生年月日"])

# 要素の削除
del purple["ニックネーム"]
print(purple)

def convert_number(num):
    # アラビア数字とローマ数字の対応表をディクショナリに定義
    roman_nums = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V",
     6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
    # ディクショナリのキーとして引数の整数が存在していたら
    # キーに対応る値を戻り値にする
    if num in roman_nums:
        return roman_nums[num]
    else:
        print "[変換できません]"

purple = {"ニックネーム": "れにちゃん",
"出身地": "神奈川県",
"キャッチフレーズ": "感電少女",
"生年月日": "1993年6月21日"}
for key in purple:
    print(key, purple[key])
