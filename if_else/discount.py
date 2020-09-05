cost=int(input("cost="))
discount=cost*10/100
if cost>1000:
    print(cost-discount)
else:
    print(cost)