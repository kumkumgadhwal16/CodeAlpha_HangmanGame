# hangman game

import random

# List of words for the game
words = ["python", "developer", "hangman", "game","intern"]

# Randomly choose a word from the list
word = random.choice(words)
guessed_letters = []
attempts = 6  # Number of chances

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while attempts > 0:

    # Display the word with guessed letters and underscores
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("\nWord:", " ".join(display_word))

    # Check if player guessed the whole word
    if display_word == word:
        print("\n Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f" Wrong guess! Attempts left: {attempts}")

# Game over
if attempts == 0:
    print("\n Game Over! The word was:", word)