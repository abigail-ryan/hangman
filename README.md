# HANGMAN
[View my live app here](https://abi-ryan-pp3-hangman-9dd3119b68fb.herokuapp.com/)

The popular pen and paper word guessing game, Hangman, can now be played in digital format using my Python project. Users play a random word every time, and have limited guesses to get it right.

![Screenshot of Hangman app terminal](documentation/hangman_app_terminal_screenshot.png)

## Contents
* [Project Goals](#project-goals)
  * [Primary Goal](#primary-goal)
  * [Visitor Goals](#visitor-goal)
* [User Stories](#user-stories)
* [UX Design](#ux-design)
  * [Strategy](#strategy)
  *	[Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
    * [Flowchart](#flowchart)
  * [Surface](#surface)
* [Project Features](#project-features)
  * [Welcome](#welcome)
  * [Game](#game)
  * [Game Over](#game-over)
  * [Validating User input](#validating-user-input)
* [Future Features](#future-features)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Technologies and Programs used](#frameworks-libraries-technologies-and-programs-used)
* [Testing](#testing)
* [Deployment](#deployment)
  * [Deploying to Heroku](#Deploying-to-heroku)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Clone the GitHub Repository](#clone-the-github-repository)
* [Credits](#credits)
  * [Content and Code References](#content-and-code-references)
* [Acknowledgements](#acknowledgements)  
         
 
___

### Project Goals

#### Primary Goal

The goal is to create an interactive and entertaining word guessing game for users of all ages to play online, with the traditional Hangman artwork. Each game will generate a random word and ask the player to guess a letter. Players will be prompted when the letter they guessed is not part of the hidden word to try again, and congratulated when their guess is correct. The amount of remaining guesses decreases with every wrong guess and a new piece of the Hangman is added. When the Hangman is complete, players have lost the game. 

#### Visitor Goal

Visitors to Hangman will be able to play a digital version of the traditional Hangman game against the computer. 


___

### User Stories

* A user can easily identify what that this is a Hangman game.
* A user can understand the game rules.
* A user can choose to start the game when they are ready.
* A user is provided with clear instructions throughout the game.
* A user can immediately see if their guess is correct/incorrect.
* A user can exit the game at any point.
* A user can start the game over again.


___

### UX Design

#### Strategy

* The Hangman game needs to be simple but fun and interactive. 
* The rules must effectively outline to the user how to play the game.
* The Hangman game needs to be started when the user is ready.
* The number of remaining guesses must be displayed to the player throughout.
* The player must be notified when they have guessed an incorrect/correct letter.
* The player must be notified if they have won/lost the game.
* The player must be able to play the game again or exit back to the start.

#### Scope

* The objective of the Hangman game is to get players to guess the hidden word by guessing individual letters one at a time.
* The traditional pen and paper Hangman artwork must be included, and be completed section by section when the player guesses are incorrect.

#### Structure

* As this Hangman game works on the command line interface, information will be displayed to the player depending on their input/ requests.
* The game rules are displayed and the player is asked if they want to play, and given the Yes/No input options.
* When the game begins, the player is shown an empty gallows as well as a row of empty letter placeholders, in accordance to the hidden word.
* When the player guesses a letter, if it is correct the letters are revealed in the placeholders. The amount of remaining guesses in unaffected.
* When the player guesses an incorrect letter, the player is notified this letter is not in the hidden word, a section is added to the Hangman and the number of remaining guesses is decreased. 
* When the player runs out of guesses and completes the Hangman, they have lost the game.
* If the player guesses the full word correctly before running out of guesses, they have won the game.

#### Skeleton
##### Flowchart
I created a concept flowchart for my Hangman game using Lucid Chart.

![Screenshot of Hangman concept lucidchart](documentation/lucidchart_hangman.png)

#### Surface
* Due to the nature of this project, there was no design required. However, I created the Hangman logo using ASCII banner maker and also included the Hangman Gallows on startup of the program.
* The game rules are displayed underneath the logo before the user is asked if they would like to play, and prompted to input Yes/No.

<details>
<summary>Hangman Logo Banner</summary>
<br>

![Screenshot of Hangman Logo Banner](documentation/ascii_hangman_banner.png)

</details>


___

### Project Features

#### Welcome

The player is presented with the Welcome screen and shown the game rules. The player is asked if they would like to play. 

![Screenshot of Hangman App](documentation/hangman_app_terminal_screenshot.png)

If the user inputs N the program ends with a feedback message.

![Screenshot of start feedback message](documentation/hangman_start_player_input_no.png)

If the user inputs Y it starts the game.

#### Game

The player is shown the empty Hangman Gallows along with the placeholders of the hidden word. The player is prompted to enter a letter.

![Screenshot of Hangman game start](documentation/hangman_game_board_empty.png)

Once a letter is guessed the player receives feedback if their guess is in the word, and also a list of the letters they have already guessed so far.

![Screenshot of Hangman game letter guesses](documentation/hangman_game_board_letter_guessed.png)

<details>
<summary>When the guessed letter is not in the word</summary>
<br>

The player is notified that their guess is not in the word. This letter is then added to the list of letters already guessed.

![Screenshot of incorrect letter guess](documentation/hangman_incorrect_letter.png)

</details>

<details>
<summary>When the player guesses the same letter again</summary>
<br>

The player is notified that they have already guessed this letter and prompted to try again.

![Screenshot of already guessed letter](documentation/hangman_already_guessed_letter.png)

</details>

#### Game Over

Win - If the player guesses the full word correctly they have won the game, and are congratulated.

![Screenshot of player wins](documentation/hangman_you_win.png)

Lose - If the player runs out of guesses and completes the Hangman, they have lost the game and show what the hidden word was.

![Screenshot of player loses](documentation/hangman_you_lose.png)

The player is asked if they would like to play again; if so the program runs again and new random word is generated. If the player chooses not to play again they receive a goodbye message.

![Screenshot of goodbye message](documentation/hangman_game_over_goodbye.png)

#### Validating User input

If the player enters an invalid input the game notifies the player and requests they enter the correct input.

<details>
<summary>Validating user input</summary>
<br>

Player recieves notice if they have tried to input anything other than Y or N on program startup.

![Screenshot of validating player input start game](documentation/hangman_start_validation.png)

The player recieves notice if they have tried to input anything other than a letter of the alphabet during game play.

![Screenshot of validating player input start game](documentation/hangman_letter_guess_validation.png)

</details>


___

### Future Features


___

### Technologies Used

#### Languages

#### Frameworks, Libraries, Technologies and Programs used


___

### Testing


___

### Deployment

#### Deploying to Heroku

#### Forking the GitHub Repository

#### Clone the GitHub Repository


___

### Credits

#### Content and Code References


___

### Acknowledgements


___
