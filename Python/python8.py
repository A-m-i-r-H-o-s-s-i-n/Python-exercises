import time
from os import system
while True:
    choice = input("Do you want to start? (y/n)")
    if 'y' in choice.lower():
        hovur = int(input("Enter Amount of hour: "))
        minutes = int(input("Enter Amount of minutes: "))
        seconds = int(input("Enter Amount of seconds: "))
        total = hovur * 60 * 60 + minutes * 60 + seconds
        print("Timer start now...")
        time.sleep(1)
        while total >= 1:
            print(total)
            total-=1
            time.sleep(1)
            system('cls')
        print("Timer ended...")
    elif 'n' in choice.lower():
        print("Godbuy...")
        break
    else:
        print("Invalid input...")