import requests
import json
import random
x=requests.get('http://saral.navgurukul.org/api/courses')
a=(x.text)
data= json.loads(a)
store_data=data["availableCourses"]
#first api for course names
def my_courses(store_data): 
	for i in range(0,len(store_data)):
		print(i+1,"**",store_data[i]["name"],store_data[i]["id"],store_data[i]["type"])
my_courses(store_data)

def user_input(store_data):
# taking user input for selecting particular course
	for j in range(0,len(store_data)):
		print(store_data[user-1]["name"],store_data[user-1]["id"],store_data[user-1]["type"])
		# a=(store_data[user]["id"])
		break
user=int(input("enter num for which courses you want="))
user_input(store_data)
 			
def details(store_data):
	select_id=store_data[user-1]["id"]
	exercises=requests.get('http://saral.navgurukul.org/api/courses/'+select_id+'/exercises')
	exercises_text=(exercises.text)
	topic = json.loads(exercises_text)
	my_data=topic["data"]
	for k in range(0,len(my_data)):
		# for topics under selected course
		print(k+1,my_data[k]["name"])
		for d in range(0,len(my_data)):
			s=my_data[k]["childExercises"]
				# sub_topices of selcted courses
			for sub in range(0,len(s)):
				w=s[sub]["name"]
				print(" ","#",s[sub]["name"])
						# questions under sub_topices under selected courses
			break
	choice=int(input("enter which question you want to see="))
	print("<<<<<*******   Our Content   ********>>>>>>>>")
	for k in range(0,len(my_data)):
		# for topics under selected course
		print(k,my_data[choice-1]["name"])
		break
	for d in range(0,len(my_data[choice -1])):
		s=my_data[choice-1]["childExercises"]
				# sub_topices of selcted courses
		for sub in range(0,len(s)):
			w=s[sub]["name"]
			print(sub+1,s[sub]["name"])
		break
	
	count=int(input("enter the number="))
	print("####------------ Our Question ------------#####")
	b=my_data[choice-1]["slug"]
	url=requests.get('http://saral.navgurukul.org/api/courses/'+select_id+'/exercise/getBySlug?slug='+b)
	url_txt=url.text
	my_file=json.loads(url_txt)
	content=my_file["content"]
	print(content,end="")
	# subtopices under slug content
	# for our parent -childxercise
	w=my_data[choice-1]["childExercises"]
	undr=requests.get('http://saral.navgurukul.org/api/courses/'+select_id+'/exercise/getBySlug?slug='+w[count-1]["slug"])
	undr=undr.text
	file=json.loads(undr)
	c=file["content"]
	print(c,end="")


	n=0
	while n <=len(my_data):
		s=my_data[n]["childExercises"]
		j=0
		while j<len(my_data[n]):

			next_previous=input("enter which you want up/next/previous= u/n/p/r=")
			if next_previous=="n":
				w=my_data[choice-1]["childExercises"]
				undr=requests.get('http://saral.navgurukul.org/api/courses/'+select_id+'/exercise/getBySlug?slug='+w[count+j]["slug"])
				undr=undr.text
				file=json.loads(undr)
				d=count+j
				c=file["content"]
				print("--- Our Next Q uestion---",c,end="")
			
			elif next_previous=="p":
				w=my_data[choice-1]["childExercises"]
				undr=requests.get('http://saral.navgurukul.org/api/courses/'+select_id+'/exercise/getBySlug?slug='+w[d-1]["slug"])
				undr=undr.text
				file=json.loads(undr)
				c=file["content"]
				print("----Our Previous Question----",c,end="")

			elif next_previous=='r':
				x= random.randint(0,len(my_data))
				b=(my_data[x]["slug"])
				url=requests.get('http://saral.navgurukul.org/api/courses/'+select_id+'/exercise/getBySlug?slug='+b)
				url_txt=url.text
				my_file=json.loads(url_txt)
				content=my_file["content"]
				print(content,end="")
			
			elif next_previous=='u':
				print("..<<<<<<----- Again Menu------>>>..")
				our_menu=my_courses(store_data)
				selection=user_input(store_data)
				our_child=details(store_data)
			j+=1
		else:
			print("data has been over")
		n+=1
	else:
		print("data has been over")

details(store_data)

