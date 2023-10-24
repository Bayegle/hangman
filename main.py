import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        print("\n The mistery word has" + str(num_lives) + "characters")

        self.word = random.choice(word_list)
        print("\n The word to guess is : " + self.word)
        self.word_guessed = []
        lenword = len(self.word)
        for i in range(lenword):
            self.word_guessed.append("_")
        wordsplit = []
        wordsplit.extend(self.word)
        setword = set(wordsplit)
        self.num_letters = len(setword)
        self.list_of_guesses = set()
        print("\n Word guessed 0 is : " + str(self.word_guessed))

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("\n Good guess!" + guess + " is in the word.")
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives -1
            print("\n Sorry, " + guess + " is not in the word.")
            print("\n You have " + str(self.num_lives) + "lives left.")
        print("\n Word guessed is : " + str(self.word_guessed))
    def guess_letter(self, guess):

        print("\n my guess is: " + guess)
        diagnostic = True

        if not (len(guess) == 1 and guess.isalpha()):
            print("\n Invalid letter. Please, enter a single alphabetical character.")
            diagnostic = True
        elif guess in self.list_of_guesses:
            print("\n You already tried that letter!")
            diagnostic = True
        else:
            print("\n Good guess not used before")
            self.list_of_guesses.add(guess)
            diagnostic = False
        print("\n List of guesses is : ")
        print(self.list_of_guesses)
        return diagnostic

    def ask_for_input(self):
        invalid_input = True
        guess = None
        while invalid_input:
            guess = input("enter single letter")
            invalid_input = self.guess_letter(guess)

        return guess
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    isAlive = True

    while(isAlive):
        guess = game.ask_for_input()
        game.check_guess(guess)
        if game.num_lives == 0 :
            print('\n You lost!')
            isAlive = False
        elif game.num_lives > 0 and game.num_letters > 0:
            print('\n Game continue')
        else:
             # game.num_lives > 0 and game.num_letters == 0:
             print('\n Congratulations. You won the game!')
             isAlive = False




if __name__ == '__main__':
    word_list = ["bananas", "apples", "oranges", "pineaples", "watermelon"]
    #word_list = ["pineaples"]
    play_game(word_list)
    print(" GOOD BYE ")


