
print("Welcome to Hangman")


def print_logo():
    """
    Prints the hangman logo when the program is run
    """
    logo = r"""
.  .  ,.  .  .  ,-. .   ,  ,.  .  . 
|  | /  \ |\ | /    |\ /| /  \ |\ | 
|--| |--| | \| | -. | V | |--| | \| 
|  | |  | |  | \  | |   | |  | |  | 
'  ' '  ' '  '  `-' '   ' '  ' '  '                             
    """
    print(logo)

print("Game Rules:")
print("- The computer generates a random word and you have to guess it letter by letter.")
print("- If you guess the correct letter, it will be placed on the game board.")
print("- If you complete the word you win the game.")
print("- If you guess the wrong letter, you'll lose a guess & add a piece to the Hangman.")
print("- If you use up all your guesses with wrong letters, and the Hangman is complete, you lose the game.\n")

play = input("Do you want to play? Enter 'Y' for yes or 'N' for no: \n").upper()
