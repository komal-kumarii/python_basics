year= int (input("enter the year"))
if year%100==0:
    print(year//100+1,"century")
else:
    print("1st century")