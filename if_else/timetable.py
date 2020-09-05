day_duration=input("day_duration=")
time=float(input('timing='))
if day_duration=="morning":
    if time>= 6.15 and time<7.00 :
        print("exercise")
    elif time<= 8.30:
        print("breakfast")
    elif time>=8.30 and time<1.00 :
        print("class time")
elif day_duration=="afternoon":
    if time>1.00 and time<=3.00:
        print("lunch break")
    elif time>=3.00 and time <5.00:
        print("english time")
elif day_duration=="evening":
    if time>5.00 and time<=6.30:
        print("milk break")
else:
    if time>6.30 and time<9.30:
        print("coding")
    else:
        print("dinner")