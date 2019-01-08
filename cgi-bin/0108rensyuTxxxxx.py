#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#ヘッダ情報を入力
print("Content-Type: text/html; charset=utf-8")
# ヘッダと本体データを区切る空行
print("")
# 本体のデータを出力
print("<html><head><meta charset='utf-8'><body>")
print("聞くことに早く語ることに遅くあるべき")
print("</body></html>")

import random
# ランダムな数を取得
no = random.randint(1, 6)
# 画面に出力
print("""
<html>
<head><title>Dice</title></hechad>
<body>
    <h1>{num}</h1>
</body>
""".format(num=no)) #p177のformat()メソッド

import cgi
print("<pre>")
# URLパラメータを取得する
form = cgi.FieldStorage()
# 特定のパラメータを取得して表示
mode = form.getvalue("mode", default="")
print("-- all params --")
for k in form.keys():
    print(k, "=", form.getvalue(k))

# エラーが出た時にエラーの内容を表示させる処理
import cgitb
cgitb.enable()
# フォームにv1とv2のデータが含まれるか？
if (not 'v1' in form) or (not 'v2' in form):
    #含まれないのでフォームを表示
    print("""
        <form>
        <input type="text" name="v1"> +
        <input type="text" name="v2">
        <input type="submit" value="計算">
        </form>
    """)
else:
    #フォームの値を取得して計算結果を表示
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        ans = int(v1) + int(v2)
    except:
        ans = 0
    print("<h1>", ans, "</h1>")
