user1=int(input("enter the num"))
user2=int(input("enter the num"))
c=[0,1,2,3,4,5,6,7,8,9]#num
index=0
while index<len(c):
    b=user1-c[index]#making divisible to user1 with user2 
    if b%user2==0:
        print(b)
        break#for exit from loop
    index+=1