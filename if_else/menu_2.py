day=input("enter day")
meal=input("meal")
if day=="monday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("rajma chawal")
    else:
        print("roti sabji")
elif day=="tuesday":
    if meal=="breakfast":
        print("poori sbji")
    elif meal=="lunch":
        print("thukka")
    else:
        print("chicken")
else:
    print("nothing")