import requests
import json
url=requests.get('http://saral.navgurukul.org/api/courses')
url_text=url.json()
my_file=(url_text)
d=json.dump(open("rew.json","w"),my_file)
store_data=my_file["availableCourses"]
for i in range(0,len(store_data)):
    print(i+1,store_data[i]["name"])
user = int(input("which courses you want to see=="))
for j in range(0,len(store_data)):
    print(store_data[user-1]["name"])
    break 
m=store_data[user]["id"]
exercises=requests.get('http://saral.navgurukul.org/api/courses/'+m+'/exercises')
exercises_text=(exercises.json())
topic = (exercises_text)
mydata=topic["data"]
for k in range(0,len(mydata)): 
    print(k+1,mydata[k]["name"])
    s=mydata[k]["childExercises"]
    for b in range(0,len(s)):
        print(" ",s[b]["name"])


