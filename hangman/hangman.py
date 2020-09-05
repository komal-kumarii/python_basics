import string
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise '''
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
	
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        # elif secret_word== guessed_word:
            # break
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    
    import string
    all_letters = string.ascii_lowercase
    letters_left=""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left=letters_left.replace(letter,"")

    return letters_left


def user_valid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False

    return True
def get_hint(secret_word,letters_guessed):
    import random
    not_guessesd_letter=[]

    index=0
    while index <len(secret_word):
        letter=secret_word[index]
        if letter not in letters_guessed:
            if letter not in not_guessesd_letter:
                not_guessesd_letter.append(letter)
        index+=1
    return (random.choice(not_guessesd_letter))


def hangman(secret_word):
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("")

    user_difficulty_level=input("At which difficulty level you want to play,[ Easy, Medium, Hard]/[a,b,c]=")
    total_lives=remaining_lives=8
    images_selection_indices=[0,1,2,3,4,5,6,7]
    if user_difficulty_level not in ["a","b","c"]:
        print("your choice has been invalid")
    else:
        if user_difficulty_level=="b":
            total_lives=remaining_lives=6
            images_selection_indices=[0,2,4,5,6,7]
        elif user_difficulty_level=="c":
            total_lives=remaining_lives=4
            images_selection_indices=[1,3,5,7]



    letters_guessed = []
    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)


        guess = input("Please guess a letter: ")
        if guess=="hint":
            letter=get_hint(secret_word,letters_guessed)
        else:
            letter = guess.lower()

        # if (not user_valid(letter)):
            # continue
        if letter in secret_word:

            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
    
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print(IMAGES[images_selection_indices[total_lives -remaining_lives]])
            print("remaining_lives=",remaining_lives-1)
            print ("") 
            letters_guessed.append(letter)
            remaining_lives-=1
    else:
        print("sorry, You ran out of guesses. The word was:",str(secret_word))   
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)