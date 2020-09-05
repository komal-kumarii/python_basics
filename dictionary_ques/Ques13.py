my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
}
max1=0
max2=0
max3=0
empty_list=[]
for i in my_dict:
	if max1<my_dict[i]:
		max1=my_dict[i]
		b=i
empty_list.append(b)
for j in my_dict:
	if max2<my_dict[j] and max1>my_dict[j]:
		max2=my_dict[j]
		c=j
empty_list.append(c)
for k in my_dict:
	if max1 >my_dict[k] and max2>my_dict[k] and max3<my_dict[k]:
		max3=my_dict[k]
		d=k
empty_list.append(d)
print(empty_list)
