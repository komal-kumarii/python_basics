question=["how many continents are there?","what is the capital of India?",
"whta is your name?"]

answers=[["5","6","7","8"],
["goa","delhi","Bhopal","chennai"],
["komal","nisha","sia","divya"],
]
solution=[3,2,1]#option wise answer
empty_list=[ ]#for appending all correct answers
index=0
another_opt=1#for second option after 5050
while index<len(question):#iterate for question
    print("Q",index+1,question[index])
    j=0
    while j<len(answers[index]):#iterate for options
        print(j+1,answers[index][j])
        j+=1
    s=int(input("ans="))#for answer 
    if s==5050:
        print(another_opt)
        print(solution[index])
        s=int(input("ans2="))#input ans after 5050
        another_opt+=1
    if s != solution[index]:
        print("game over")
        break#for exit from game
    else:
        empty_list.append(s)
    index+=1
if empty_list==solution:#for winner
    print("congratulations , you won the game")
