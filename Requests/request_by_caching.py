import requests
import json 
import os 
url=('http://saral.navgurukul.org/api/courses')

def request(ur):
        response = requests.get(ur)
        with open("coursesData.json","w") as file:
                file.write(response.text)
        return(response.json())
(request(url))

cousrses_id=[]
def exist_file(reading):
	 with open("coursesData.json","r") as file:
		 file_read=file.read()
		 my_file=json.loads(file_read)
		#  return(my_file)
		 data=my_file['availableCourses']
		 for i in range(0, len(data)):
			 print(i+1,data[i]["name"],"id:",data[i]["id"])
			 cousrses_id.append(data[i]["id"])
			#  break
		 return(cousrses_id)
exist_file(url)


def file_courses():
        if os.path.exists("coursesData.json")== True:
                data = exist_file("coursesData.json")
                exist_file(data)
                return ("data exists in our file##")
        else:
                request(url)
                data = exist_file("coursesData.json")
                exist_file(data)
                return("no data is not exists in our file")
(file_courses())

select_course=int(input("enter the id of the course which you want"))
selectedCourse=cousrses_id[select_course-1]
# print(cousrses_id[select_course-1]["name"])

second_api=('http://saral.navgurukul.org/api/courses/'+str(selectedCourse)+'/exercises')

def exer_data():
	exer_data=requests.get(second_api)
	with open (("exercise"+str(selectedCourse)+ ".json"),"w") as file:
		file.write(exer_data.text)
		exer_response=exer_data.json()
	# return(exer_response)
(exer_data())

def read_exer():
	with open (("exercise"+str(selectedCourse)+ ".json"),"r") as file:
		read_file=file.read()
		file_data=json.loads(read_file)
		f_data=file_data["data"]
		for j in range(0,len(f_data)):
			print(j+1,f_data[j]["name"])
			# for s in range(0,len(f_data)):
			under_content=f_data[j]["childExercises"]
			for k in range(0,len(under_content)):
				print(" ","**",under_content[k]["name"])

read_exer()

def file_available():
	if os.path.exists("exercise"+str(selectedCourse)+".json")==True:
		f_data=read_exer("exercise"+str(selectedCourse)+".json")
		file_available(f_data)
		return("data is available")
	
	else:
		exer_data(second_api)
		f_data=read_exer("exercise"+str(selectedCourse)+".json")
		file_available(f_data)
		return("data is not available you have to create a new file")

# file_available()
