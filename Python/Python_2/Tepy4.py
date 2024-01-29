import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "~!@#$%^&*"
number = "1234567890"
all = lower + upper + symbols + number

while True:
    print("Choose sn Option:\n\t1)Create a pessword\n\t2)Exit")
    choice = input("Enter Your: ")
    if choice == "1":
        length = int(input("Enter the length of Password: "))
        passwored = "".join((random.sample(all, length)))
        print(passwored)
    elif choice == "2":
        print("Godbuye..")
        break
    else:
        print("Your Choice is Wrong!\n")