from os import system
mylist = []

def insert():
    mydic= dict()
    mydic['id'] = input("Enter your id: ")
    mydic['name'] = input("Enter your name: ")
    mydic['family'] = input("Enter your family: ")
    mylist.append(mydic)

def show_all():
    print(f'{"id":<10}{"name":<15}{"family":<20}')
    print('='*40)
    for i in mylist:
        print(f'{i["id"]:<10}{i["name"]:<15}{i["family"]:<20}')
    input('Press Any Key To Exit.......')

def searh_by_id():
    u = input("Enter your id: ")
    print(f'{"id":<10}{"name":<15}{"family":<20}')
    print('='*40)
    for i in mylist:
        if i["id"] == u:
            print(f'{i["id"]:<10}{i["name"]:<15}{i["family"]:<20}')
    input('Press Any Key To Exit.......')  
            
def edit_by_id():
    u = input("Enter your id: ")
    for i in mylist:
        if i["id"] == u:
            while True:
                system('cls')
                print(f'{"id":<10}{"name":<15}{"family":<20}')
                print('='*40)
                print(f'{i["id"]:<10}{i["name"]:<15}{i["family"]:<20}')
                print('='*40)
                print("1\t name\n2\t family\n3\t id\n0\t Exit")
                n = input("Enter your number: ")
                if n == '1':
                    i["name"] = input("Enter name: ")
                elif n == '2':
                    i["family"] = input("Enter your family: ")
                elif n == '3':
                    i['id'] = input("Enter your id: ")
                elif n == '0':
                    break
                else:
                    print("Enter croct number!")
    input('Press Any Key To Exit.......')

def delete_by_id():
    u = input("Enter your id: ")
    print(f'{"id":<10}{"name":<15}{"family":<20}')
    print('='*40)
    for i in mylist:
        if i["id"] == u:
            print(f'{i["id"]:<10}{i["name"]:<15}{i["family"]:<20}')
            print('='*40)
            d = input("Do you want delete now? (y/n)")
            if d == 'y':
                mylist.remove(i)

def body():
    while True:
        system("cls")
        print("1\t insert\n2\t show all\n3\t searh by id\n4\t Edit by ID\n5\t Delete By id\n0\t Exit")
        user = input("Enter Your Intrest =")
        system('cls')
        match(user):
            case '1':
                insert()
            case '2':
                show_all()
            case '3':
                searh_by_id()
            case '4':
                edit_by_id()
            case '5':
                delete_by_id()
            case '0':
                print("GOOD BOY...")
                break
body()