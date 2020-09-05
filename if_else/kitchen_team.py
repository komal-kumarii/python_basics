kitchen_team=int(input("enter the num="))
health=input("health=")
if health=="good":
    if kitchen_team==1:
        print("kitchen team1 will work")
    elif kitchen_team==2:
        print("kitchen team2 will work")
    else:
        print("kitchen team 3 will work")
else:
    if kitchen_team==1:
        print("kitchen team2 will work")
    elif kitchen_team==2:
        print("kitchen team3 will work")
    else:
        print("kitchen team1 will work")