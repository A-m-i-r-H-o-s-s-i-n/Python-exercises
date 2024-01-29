import random
user_score = 0
pc_score = 0
run = True
options = ["s","k","q"]

while run:

    user_choice = input("lotfen az mavard ro ba ro antab konad \n")

    if user_choice in options:

        print("s:sang, k:kaqz, q:qehi")

        pc_choice = random.choice(options)
        print(f"pc choice {pc_choice}")

        if user_choice == pc_choice:
            print("mosave ye bar dage")
        elif user_choice == "s":
            if pc_choice == "k":
                pc_score += 1
            else:
                user_score += 1
        elif user_choice == "k":
            if pc_choice == "q":
                pc_score += 1
            else:
                user_score += 1
        elif user_choice == "q":
            if pc_choice == "s":
                pc_score += 1
            else:
                user_score += 1

        print(f"user: {user_score} - pc: {pc_score} => berim daste badi")
        if user_score == 3 or pc_score == 3:
            if user_score == 3:
                print("USER BORD")
            else:
                print("PC BORD")
            run = False
        else:
            print("lotfan az ben gozanh ha anthab konad")