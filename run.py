import random

word_bank = ["elephant", "computer", "sunshine", "butterfly", "adventure", "chocolate", 
"rainbow", "guitar", "ocean", "watermelon", "universe", "mountain", "fireworks", "friendship",
 "beach", "pizza", "dragon", "galaxy", "starfish", "vacation", "jelly", "jungle", "mystery", 
 "serenity", "waterfall", "wonderland", "carnival", "treasure", "dreamcatcher", "lighthouse", 
 "mermaid", "whisper", "adventure", "harmony", "midnight", "symphony", "twilight", "whisper", "blossom",
 "enchanted", "radiance", "velvet", "bird", "fish", "moon", "star", "tree", "rain", "book", "time"]


def get_random_word():
    """
    Chooses random word from word bank list and returns it in uppercase.
    """
    word = random.choice(word_bank)
    return word.upper()

def print_hangman(remaining_guesses):
    """
    Prints hangman sections depending on number of wrong letters guessed.
    """
    if (remaining_guesses == 6):
        print("+---+ ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("========")
    elif (remaining_guesses == 5):
        print("+---+ ")
        print("|   0  ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("========")
    elif (remaining_guesses == 4):
        print("+---+ ")
        print("|   0  ")
        print("|   |  ")
        print("|      ")
        print("|      ")
        print("========")
    elif (remaining_guesses == 3):
        print("+---+ ")
        print("|   0  ")
        print("|  /|  ")
        print("|      ")
        print("|      ")
        print("========")
    elif (remaining_guesses == 2):
        print("+---+ ")
        print("|   0  ")
        print("|  /|\\ ")
        print("|      ")
        print("|      ")
        print("========")
    elif (remaining_guesses == 1):
        print("+---+ ")
        print("|   0  ")
        print("|  /|\\ ")
        print("|  /   ")
        print("|      ")
        print("========")
    elif (remaining_guesses == 0):
        print("+---+ ")
        print("|   0  ")
        print("|  /|\\ ")
        print("|  / \\ ")
        print("|      ")
        print("========")

def play_game(word):
    completed_word = ["_"] * len(word)
    guessed = False
    guessed_letters = [] 
    remaining_guesses = 6
    print("Lets Play!")
    print_hangman(remaining_guesses)
    print(completed_word) 
    print("\n")
    """
    While the remining guesses are not less than 6, game runs through loop asking player to guess a letter.
    """
    while not guessed and remaining_guesses > 0:
        player_guess = input("Guess a letter: \n").upper()
        """
        Check if players guess is a letter, has already been guessed, and if guess is/is not in the hidden word.
        """
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                print(f"You already guessed {player_guess}. Try again.")
            elif player_guess not in word:
                print(f"{player_guess} is not in this word. Try again.")
                remaining_guesses -= 1
                guessed_letters.append(player_guess)
            else:
                print(f"{player_guess} is in this word!")
                guessed_letters.append(player_guess)
                word_as_list = list(completed_word)
                indices = [i for i, letter in enumerate(word) if letter == player_guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess. Try again.")
            print_hangman(remaining_guesses)
            print(completed_word) 
            print("\n")
 


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

print("    +---+ ")
print("    |   0  ")
print("    |  /|\\ ")
print("    |  / \\ ")
print("    |      ")
print("    ========")

print("Hangman Game Rules:")
print("- The computer generates a random word and you have to guess it letter by letter.")
print("- If you guess the correct letter, it will be placed on the game board.")
print("- If you complete the word you win the game.")
print("- If you guess the wrong letter, you'll lose a guess & add a piece to the Hangman.")
print("- If you use up all your guesses and the Hangman is complete, you lose the game.\n")

def play_choice():
    """
    Validates user input. Requires user to enter only Y or N.
    If user inputs invalid choice the loop runs until one of the options is selected.
    """
    while True:
        choice = input("Do you want to play? Enter 'Y' for yes or 'N' for no: \n").upper()
        if choice == "Y" :
            word = get_random_word()
            play_game(word)
        elif choice == "N" :
            print("Sorry to see you go. Come back and play another time!")
            break
        else:
            print("Invalid option.")
play_choice()



def main():
    word = get_random_word()
    play_game(word)
   



       


