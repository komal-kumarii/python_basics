my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
}
max1=my_dict["a"]
max2=my_dict["a"]
max3=my_dict["a"]
empty_lis=[]
for i in my_dict.values():
	if max1 <i:
		max1=i
	for j in my_dict.values():
		if max1>j and max2<j:
			max2=j
		for k in my_dict.values():
			if max1>k and max2>k and max3<k:
				max3=k
empty_lis.append(max3)
empty_lis.append(max2)
empty_lis.append(max1)
print(empty_lis)
