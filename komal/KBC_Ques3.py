question=["how many continents are there?","what is the capital of India?",
"what is your name?"]
answers=[["5","6","7","8"],
["goa","delhi","Bhopal","chennai"],
["komal","nisha","sia","divya"],
]
solution=[3,2,1]
index=0#for iterate question list
while index<len(question):
    print("Q",index+1,question[index])
    j=0
    while j<len(answers[index]):#iterate for answer list
        print(j+1,answers[index][j])
        j+=1
    s=int(input("ans="))#for writing answer
    if s == solution[index]:#for check answer
        print("congratulations,correct")
    else:
        print("wrong")
    index+=1#for next question