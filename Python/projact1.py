from os import system
def my_sum(a ,b):
    result = a + b
    print(f"{a}+{b}= {result}")
def my_sub(a,b):
    result = a - b
    print(f"{a}-{b}= {result}")
def my_mul(a , b):
    result = a * b
    print(f"{a}*{b}= {result}")
def my_div(a ,b):
     result = a / b
     print(f"{a}/{b}= {result}")

system("cls")

a = int(input("adade avale morede nazar ra vared konid \n"))
b = int(input("adade dovaom morede nazar ra vared konid \n"))

operator = input("amelgar mored nazar khon ra vared konid \n")


if operator == "+":
    my_sum(a , b)
elif operator == "-":
    my_sub(a ,b)
elif operator == "*":
    my_mul
elif operator == "/":
   my_div
else:
    print("amleat mored nzar drost nast! ")