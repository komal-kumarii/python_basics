question=["how many continents are there?","what is the capital of India?",
"what is your name?"]
answers=[["5","6","7","8"],
["goa","delhi","Bhopal","chennai"],
["komal","nisha","sia","divya"]]
solution=[3,2,1]
index=0
empty_list=[ ]
while index<len(question):#for printing question
    print("Q",index+1,question[index])
    j=0#for options
    while j<len(answers[index]):
        print(j+1,answers[index][j])
        j+=1
    s=int(input("ans2="))#for writing answer
    if s==solution[index]:
        empty_list.append(s)
    else:
        print("Game Over")#exit from game
        break
    index+=1#for next question
if empty_list==solution:#for winner
    print("congratulations, you won the game")