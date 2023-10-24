import random

def create_word():
    word_list = ["bananas", "apples", "oranges", "pineaples", "watermelon"]
    word = random.choice(word_list)
    print(word_list)
    return word




def guess_letter():
    guess = input("enter single letter")
    print("my guess is: " + guess)
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        return guess
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return None



def check_guess(guess):
    myword = create_word()
    guess = guess.lower()
    return (guess in myword)

def ask_for_input():
    invalid_input = True
    guess = None
    while invalid_input:
        guess = guess_letter()
        if guess is not None:
            invalid_input = False
    return guess

def secret_word():

    guess = ask_for_input()
    if check_guess(guess):
        print("Good guess!" + guess + "is in the word.")
    else:
        print( "Sorry," + guess + "is not in the word. Try again.")





















