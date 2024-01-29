def repeat(number, digit):

    cont = 0
    while number>0:
        if number % 10 == digit:
            cont +=1 
        number //= 10
    return cont


number = int(input("Enter number: "))

digit = int(input("Enter number: "))

print(digit,"Repeat", repeat(number, digit), "times")

#===================================================================

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(fact(int(input("Enter number: "))))

#===================================================================

def sum_fact(n):
    sum = 0
    for i in range(1, n+1):
        sum += fact(i)
    return sum

print(sum_fact(4))