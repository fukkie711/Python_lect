# coding:utf-8
def convert_currency(price, currency="円をドルに"):
    if currency == "円をドルに":
        result = price * 0.0088
    elif currency == "ドルを円に":
        result = price * 113.02
    print("為替は：", currency)
    print("元の値段は：", price)
    print("価格は：", result)

convert_currency(10000)
convert_currency(currency="ドルを円に", price=100)
