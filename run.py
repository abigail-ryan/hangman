import os
import random

word_bank = ["elephant", "computer", "sunshine", "butterfly",
             "adventure", "chocolate", "rainbow", "guitar", "ocean",
             "watermelon", "universe", "mountain", "fireworks", "friendship",
             "beach", "pizza", "dragon", "galaxy", "starfish", "vacation",
             "jelly", "jungle", "mystery", "serenity", "waterfall",
             "wonderland", "carnival", "treasure", "dreamcatcher",
             "lighthouse", "mermaid", "adventure", "harmony",
             "midnight", "symphony", "twilight", "whisper", "blossom",
             "enchanted", "radiance", "velvet", "bird", "fish", "moon",
             "star", "tree", "rain", "book", "time"]


def get_random_word():
    """
    Chooses random word from word bank list and returns it in uppercase.
    """
    word = random.choice(word_bank)
    return word.upper()


# Clearing terminal code credited to: https://github.com/OleksiiKova/hangman

def clear_screen():
    """
    Clears the welcome screen and only shows the game play to the user.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Hangman artwork, altered for my project, credited to:
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

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


def play_again():
    """
    Asks the player if they want to play again after they win/lose.
    """
    while True:
        play_again = input("Do you want to play again? (Y/N): \n").upper()
        if play_again == "Y":
            clear_screen()
            word = get_random_word()
            play_game(word)
            return True
        elif play_again == "N":
            print("Thank you for playing. Goodbye!")
            return False
            break
        else:
            print("Oops, That's not an option. Please enter 'Y' or 'N'.")


# Hangman basic game functionality code altered for my project,
# credited to: https://www.youtube.com/watch?v=m4nEnsavl6w

def play_game(word):
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    remaining_guesses = 6
    print("Let's Play!")
    print_hangman(remaining_guesses)
    print(completed_word)
    print("\n")
    """
    While the remining guesses are greater than 0, the game runs through
    the loop asking player to guess a letter.
    """
    while not guessed and remaining_guesses > 0:
        player_guess = input("Guess a letter: \n").upper()
        """
        Checks if players guess is a letter, has already been guessed, and
        if the guess is/is not in the hidden word.
        Displays a list of letters the player has already guessed.
        Displays the hangman with added sections if guessed letters are
        not in the word.
        """
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                print(f"You already guessed {player_guess}. Try again.")
            elif player_guess not in word:
                print_hangman(remaining_guesses)
                print(completed_word)
                print("\n")
                print(f"{player_guess} is not in this word. Try again.")
                remaining_guesses -= 1
                guessed_letters.append(player_guess)
                print(f"Letters guessed so far: {','.join(guessed_letters)}\n")
            else:
                guessed_letters.append(player_guess)
                """
                Checks if the correctly guessed letter is anywhere within
                the hidden word and places all instances of correct letter
                in the placeholders.
                """
                word_as_list = list(completed_word)
                indices = [i for i, x in enumerate(word) if x == player_guess]
                for index in indices:
                    word_as_list[index] = player_guess
                completed_word = "".join(word_as_list)
                print_hangman(remaining_guesses)
                print(completed_word)
                print("\n")
                print(f"Yay! There is 1 or more {player_guess} in this word!")
                print(f"Letters guessed so far: {','.join(guessed_letters)}\n")

                if "_" not in completed_word:
                    guessed = True

        else:
            print("Oops that's not a valid guess. Please only enter letters.")
            print("\n")

    if not guessed:
        print_hangman(remaining_guesses)
        print(f"Sorry! You lost the game. The hidden word was {word}")
    else:
        print(f"Congratulations, you guessed the word: {word}. You win!")


# Hangman logo banner sourced from: https://manytools.org/
# hacker-tools/ascii-banner/

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
print("- The computer picks a random word, you guess it letter by letter.")
print("- If you guess the correct letter, it is placed on the game board.")
print("- If you complete the word you win the game.")
print("- If you guess the wrong letter you'll add a piece to the Hangman.")
print("- If you use all your guesses & complete the Hangman, you lose.\n")
print("Do you want to play?")


def play_choice():
    """
    Validates user input. Requires user to enter only Y or N.
    If user inputs invalid choice the loop runs until one of
    the options is selected.
    """
    while True:
        choice = input("Enter 'Y' for yes or 'N' for no: \n").upper()
        if choice == "Y":
            clear_screen()
            word = get_random_word()
            play_game(word)
            if not play_again():
                break
        elif choice == "N":
            print("Sorry to see you go. Come back and play another time!")
            break
        else:
            print("Oops, that's not an option.")


def main():
    play_choice()


main()
