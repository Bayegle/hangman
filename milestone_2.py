import random

def my_list_test():
    word_list = ["bananas", "apples", "oranges", "pineaples", "watermelon"]
    word = random.choice(word_list)
    print(word_list)
    print(word)

def guess_letter():
    guess = input("enter single letter")
    #print("my guess is: " + guess)
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")




