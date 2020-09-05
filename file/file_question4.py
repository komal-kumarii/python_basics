my_file=open("people_exercise.txt")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("others.txt","w")
for data in my_file:
	if "delhi" in data:
		file1.write(data)
		file1.write("\n")
	elif "shimla" in datas:
		file2.write(data)
		file2.write("\n")
	else:
		file3.write(data)
		file3.write("\n")
file1.close()
file2.close()
file3.close()

