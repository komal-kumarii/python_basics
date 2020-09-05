import random
def getSecretNum(numDigits):
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ""
  for i in range(numDigits):
    secretNum +=str(numbers[i])
  return(secretNum)

def getClue(guess,secretNum):
  clue=[]
  if guess == secretNum:
    return('You got it!')
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      clue.append('Fermi')
    elif guess[i] in secretNum:
      clue.append('Pico')
    else:
      clue.append("none")
  return(clue)

def isOnlyDigits(num):
  if num == "":
    return True

  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return False


def playAgain(play_again):
  return play_again.lower()
numDigits = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.',(numDigits))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')
while True:
  secretNum = getSecretNum(numDigits)                                                                                                                                                                 
  print('I have thought up a number. You have %s guesses to get it.',(MAXGUESS))
  guess=input("enter the num=")
  clue= getClue(guess,secretNum)
  print(clue)
  numGuesses= 1
  while numGuesses <= MAXGUESS:
    if secretNum!= numDigits or not isOnlyDigits(guess):
      print('Guess' , (numGuesses))
    guess =input("Guess Again=")
    clue = getClue(guess, secretNum)
    print(clue)
    numGuesses += 1
  if guess == secretNum:
      break
  if numGuesses >MAXGUESS:
      print ('You ran out of guesses. The answer was ',secretNum)
  play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
  if play_again == 'Y':
        print("okk")
  elif play_again == 'N':
        break
  playAgain(play_again)
  