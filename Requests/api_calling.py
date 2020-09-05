import requests
import json
x=requests.get('http://saral.navgurukul.org/api/courses')
a=(x.text)
data= json.loads(a)
store_data=data["availableCourses"]
	
def my_courses(store_data): 
	for i in range(0,len(store_data)): 
		print(i,store_data[i]["name"],store_data[i]["id"],store_data[i]["type"])
my_courses(store_data)


user=int(input("enter num for which courses you want="))
for i in range(0,len(store_data)):
	print(store_data[user]["name"],store_data[user]["id"],store_data[user]["type"])
	a=(store_data[user]["id"])
	break
print()

exercises=requests.get('http://saral.navgurukul.org/api/courses/'+a+'/exercises')
exercises_text=(exercises.text)
topic = json.loads(exercises_text)
my_data=topic["data"]
user1=input("Are you want to see the internal topices in your courses : yes/no=")
 			
def details(my_data):
	for k in range(0,len(my_data)):
		if user1=="yes": 
			print(k+1,my_data[k]["name"])
			for d in range(0,len(my_data[k])):
				s=my_data[k]["childExercises"]
				for sub in range(0,len(s)):
						print(" ",s[sub]["name"])
				break
details(my_data)

# slug=requests.get('http://saral.navgurukul.org/api/courses/'+a+'/exercise/getBySlug?slug='+s[sub]["name"])
# slug_txt=(slug.text)
# mera_data= json.loads(slug_txt)
# var=mera_data["slug"]
# def my_slug(var):
# 	for l in range(0,len(var)):
# 		print(var[l])
# choice=int(input("which ques you want to see, enter your ques number="))
# my_slug(var)

