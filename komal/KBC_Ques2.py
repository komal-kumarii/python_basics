question=["how many continents are there?",
"what is the capital of India?","what is your name?"]
answers=[["5","6","7","8"],
["goa","delhi","Bhopal","chennai"],
["komal","nisha","sia","divya"],
]
index=0
while index<len(question):#iterate for question
    print("Q",index+1,question[index])
    j=0
    while j<=len(answers):#iterate for answer
        print(j+1,answers[index][j])#for printing option
        j+=1
    print( )
    index+=1#for next question