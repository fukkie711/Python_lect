# 課題1
def calc_tax(price):
    tax_rate = 0.08
    tax = price * tax_rate
    price_include_tax = price + tax
    return price_include_tax

print(calc_tax(2700))

# 課題2
from random import randint
times_of_simulate = 1000

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for i in range(times_of_simulate):
    i = randint(1, 6)
    if i == 1:
        one += 1
    elif i == 2:
        two += 1
    elif i == 3:
        three += 1
    elif i == 4:
        four += 1
    elif i == 5:
        five += 1
    else:
        six += 1
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)
print("five:", five)
print("six:", six)

# 課題3
def dice_num_simulation(times):
     times_of_simulate = times
     dice = [0, 0, 0, 0, 0, 0]

     for i in range(times_of_simulate):
         i = randint(1, 6)
         if i == 1:
             dice[0] += 1
         elif i == 2:
             dice[1] += 1
         elif i == 3:
             dice[2] += 1
         elif i == 4:
             dice[3] += 1
         elif i == 5:
             dice[4] += 1
         else:
             dice[5] += 1
     print("simulation kaisuu:", times_of_simulate)
     print("one:", dice[0])
     print("two:", dice[1])
     print("three:", dice[2])
     print("four:", dice[3])
     print("five:", dice[4])
     print("six:", dice[5])

print(dice_num_simulation(500))

# 課題4
from matplotlib import pyplot
pyplot.bar([1, 2, 3, 4, 5, 6], [one, two, three, four, five, six])
