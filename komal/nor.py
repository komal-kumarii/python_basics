def my_fun(string):
	word=string.split()
	a=0
	b=""
	while a<len(word):
		if word[a]==" ":
			c=word[a].upper()
			b+=(c)
			a+=1
			if word[a]==c:
				continue
		b+=(word[a])
		a+=1
	return(b)
print(my_fun("i am komal"))
