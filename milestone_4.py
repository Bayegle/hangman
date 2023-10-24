import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        print("The mistery word has" + str(num_lives) + "characters")
        self.word = random.choice(word_list)
        self.word_guessed = []
        for i in range(1,len(self.word)):
            self.word_guessed.append("_")
        wordsplit = []
        wordsplit.extend(self.word)
        setword = set(wordsplit)
        self.num_letters = len(setword)
        self.list_of_guesses = set()

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!" + guess + "is in the word.")
            for i in range(0, len(self.word)-1):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives -1
            print(" Sorry, " + guess + " is not in the word.")
            print("You have " + str(self.num_lives) + "lives left.")

    def guess_letter(self,guess):

        print("my guess is: " + guess)
        if not (len(guess) == 1 and guess.isalpha()):
            print("Invalid letter. Please, enter a single alphabetical character.")

        elif guess in self.list_of_guesses:
            print("You already tried that letter!")

        else:
            print(" Good guess not used before")
            self.list_of_guesses.add(guess)


    def ask_for_input(self):
        invalid_input = True
        guess = None
        while invalid_input:
            guess = self.guess_letter()
            if guess is not None:
                invalid_input = False
        return guess






