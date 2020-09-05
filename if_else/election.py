day=input("day")
name1= input("name=")
name2=input("name=")
name3=input("name=")
vote1=int(input("%of vote get to name1="))
vote2=int(input("% of vote get to name2="))
vote3= int(input("% of vote get to name3="))
work="work"
if day=="monday":
    print("Disco will elected")
    print(work,"=","Discipline coordinator")
    if vote1 >vote2 and vote1>vote3:
        print(name1,"will br dicso")
    elif vote2>vote1 and vote2>vote3:
        print(name2,"will be disco")
    else:
        print(name3,"will be disco")
