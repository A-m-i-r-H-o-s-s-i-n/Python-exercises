number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"Even number {number}")
else:
    print(f"Odd number {number}")

#==========================================

value = int(input("Enter a number: "))

if value > 0:
    print(f"positive number {value}")
elif value < 0:
    print(f"negative number {value}")
else:
    print(f"zero {value}")

#==========================================

my_string = input("Enter: ")
if not my_string:
    print("Empty entry")
else:
    print("The entry is not empty")

#==============================================

number = int(input("Enter a number between 10 and 30:\n"))
lower_limit = 10
upper_limit = 30
if lower_limit <= number <= upper_limit:
    print(f"The {number} is in the specified range")
else:
    print(f"The {number} is in the specified range of intentions")