HANGMAN PROJET.
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
We used python to program this classic game.
The program is made up of 4 milestones and a main class which shows the game in action.
In milestone_2 we import randon and define a function named my_list_test() then in the function body we create a word_list of 5 differents fruits. We further define another function guess_letter in which we invite the user to enter a valid letter. we implemented the following code in the body of our function

guess = input("enter single letter")
    #print("my guess is: " + guess)
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
        
In milestone_3, milestone_4 and mileston_5 we define others functions including ask_for_input(), check_guess(), create_word(), and create_word. 

We update our code as we progress making sure readability is good. We copy the code in milestone_4 in milestone_5, then update it.

we make sure all functionalities are added and tested in the play_game function before we test the game at the end of milestone_5.


 
