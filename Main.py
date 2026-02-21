# import all modules to the main class
import random
import art, words

lives = 6

# display logo to look good
print(art.logo)

chosenWord = random.choice(words.wordlist)
# print(chosenWord)

placeHolder = ""
wordLength = len(chosenWord)

for position in range(wordLength):
    placeHolder += "_"

print("Word to guess: " + placeHolder)

gameOver = False
correctLetters = []

while not gameOver:
    # telling user that howmany lives they have left
    print(f"**************** {lives}/6 Lives Left ****************")

    guess = input("Guess a letter: ").lower()

    # If the user has entered a word that they already guessed then tell them about it...
    if guess in correctLetters:
        print(f"You already guessed {guess}")

    display = ""

    for letter in chosenWord:
        if letter == guess:
            display += letter
            correctLetters.append(guess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"
    print("Word to guess " + display)

    # if the letter is not in the chosen word then let them know that they are loosing a chance
    if guess not in chosenWord:
        lives -= 1
        print(f"You guessed the word {guess}, That's not in the word, You lose.... :(")

        if lives == 0:
            gameOver = True
            print(f"*****************It was {chosenWord} :( You Lose! *****************")

    # if they guessed all right that huurrrreeeeeehhhhhhhhh, they win
    if "_" not in display:
        gameOver = True
        print("*************** You Win! ***************")

    print(art.stages[lives])
