import random

words = ["python", "programming", "chatbot", "computer", "science"]
word = random.choice(words)
guessed = []
tries = 6

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print("Word:", display)

    if display == word:
        print("You win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

if tries == 0:
    print("You lost. Word was:", word)
