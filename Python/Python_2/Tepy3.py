while True:
    print("Chooes Your Option: \n\t1)Encrypt\n\t2)Decryp\n\t3)Exit")
    choice = input("Your Choice: ")
    if choice == "1":
        plan_text = input("text: ")
        encrypt_text = ""
        for c in plan_text:
            x = ord(c) * 2 + 5 
            encrypt_text += chr(x)
        print("encrypt text: ",encrypt_text)
        print("="*40 +"\n")
    elif choice == "2":
        encrypt_text = input("encrypt_text: ")
        plan_text = ""
        for c in encrypt_text:
            x = (ord(c) - 5) // 2 
            plan_text += chr(x)
        print("plantext: ",plan_text)
        print("="*40 +"\n")
    elif choice == "3":
        print("Godbuyy")
        print("="*40 +"\n")
        break
    else:
        print("Your Choice is Wrong!")
