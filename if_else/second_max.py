user1=int(input("enter the num"))
user2=int(input("enter the num"))
user3=int(input("enter the num"))
if (user1>user2 or user1>user3) and (user1 <user2 or user1 <user3):
    print("user1 is second max")
elif (user2>user1 or user2>user3)and (user2<user1 or user2 <user3):
    print("user2 is second max")
else:
    print("user3 is second max")