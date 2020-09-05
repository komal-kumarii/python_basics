banks_list=["kotak","HDFC","RBL","SBI","Bank of baroda"]
file=open("file_question3.txt","w")
for data in banks_list:
	file.write(data)
	file.write("\n")
file.close()
# print(file)
