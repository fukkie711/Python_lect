# coding:utf-8
# 関数の呼び出し，引数，戻り値の復習
int("101010", 2)       # 二進数相当の文字列を数値に変換
print(int("101010", 2))

# FizzBuzzを解く関数
def fizzbuzz(count=100, fizzmod=3, buzzmod=5):
    for cnt in range(1, count+1):             # count回繰り返し
        if cnt%fizzmod == 0 and cnt%buzzmod == 0:
            # fizzmodでもbuzzmod でも割り切れる
            print("FizzBuzz")
        elif cnt%fizzmod == 0:
            # fizzmodで割り切れる
            print("Fizz")
        elif cnt%buzzmod == 0:
            # buzzmodで割り切れる
            print("Buzz")
        else:
            # 数値を表示する
            print(cnt)
fizzbuzz() #引数を指定しない場合、デフォルト値が利用される
fizzbuzz(50, 4, 5) #引数を任意に指定できる

# キーワードを指定して引数の順番を入れ替えて見る
int(base=2, x="1010")  # int("1010", 2)と同じ
print(int(base=2, x="1010"))

# ローカル変数の挙動を確認
local_var = 1

def test_func(an_arg):
    local_var = an_arg
    print("test_func()の中 =", local_var)

test_func(200)
print("test_func()の外 =", local_var)
