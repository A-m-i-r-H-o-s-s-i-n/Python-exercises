sum = 0
#======================
number = 524
num = number % 10
sum = sum*10 + num
#======================
number = number // 10
num = number % 10
sum = sum*10 + num
#======================
number = number // 10
num = number % 10
sum = sum*10 + num
#======================
print(f'old number = 524 new number is {sum}')