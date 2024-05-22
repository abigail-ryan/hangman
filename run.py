import random

word_bank = ["elephant", "computer", "sunshine", "butterfly", "adventure", "chocolate", 
"rainbow", "guitar", "ocean", "watermelon", "universe", "mountain", "fireworks", "friendship",
 "beach", "pizza", "dragon", "galaxy", "starfish", "vacation", "jelly", "jungle", "mystery", 
 "serenity", "waterfall", "wonderland", "carnival", "treasure", "dreamcatcher", "lighthouse", 
 "mermaid", "whisper", "adventure", "harmony", "midnight", "symphony", "twilight", "whisper", "blossom",
 "enchanted", "radiance", "velvet", "bird", "fish", "moon", "star", "tree", "rain", "book", "time"]


print("Welcome to ")

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
print_logo()

print("Hangman Game Rules:")
print("- The computer generates a random word and you have to guess it letter by letter.")
print("- If you guess the correct letter, it will be placed on the game board.")
print("- If you complete the word you win the game.")
print("- If you guess the wrong letter, you'll lose a guess & add a piece to the Hangman.")
print("- If you use up all your guesses and the Hangman is complete, you lose the game.\n")

"""
Validates user input. Requires user to enter only Y or N.
If user inputs invalid choice the loop runs until one of the options is selected.
"""
while True:
    choice = input("Do you want to play? Enter 'Y' for yes or 'N' for no: \n").upper()
    if choice == "Y" :
        play_game()
    elif choice == "N" :
        print("Sorry to see you go. Come back and play another time!")
        break
    else:
        print("Invalid option.")



       


