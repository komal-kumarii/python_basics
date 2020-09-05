print("WELCOME")
language=input("select language=")
if language=="english":
    print("english is your selected language")
    pin=int(input("enter your pin="))
    if pin== 1234:
        confirm=int(input ("enter your confirmed pin"))
        if confirm==pin:
            print("okk")
            account=input("type of account=")
            amount=int(input ("withdrawal amount-="))
            if amount<10000:
                print("collect cash")
            else:
                print("transaction cancel")
        else:
            print("INVALID")
    else:
        print("invalid pin")