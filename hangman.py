import random

words_with_hints = {
    "python": "A popular programming language.",
    "elephant": "The largest land animal.",
    "guitar": "A musical instrument with strings.",
    "pizza": "A popular Italian dish with cheese and toppings.",
    "astronaut": "Someone who travels to space."
}

hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""
]

word, hint = random.choice(list(words_with_hints.items()))
attempts, guessed_letters, word_letters = 6, set(), set(word)

print(f"Welcome to Hangman!\nHint: {hint}\n{hangman_stages[0]}")

while attempts > 0 and word_letters != guessed_letters:
    print("\nWord:", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters or len(guess) != 1 or not guess.isalpha():
        print("Invalid input or already guessed.")
    elif guess in word_letters:
        guessed_letters.add(guess)
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts remaining: {attempts}")
        print(hangman_stages[6 - attempts])
    
if word_letters == guessed_letters:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Game over! The word was: {word}")
