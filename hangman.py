import random

def play_hangman():
    # Predefined words
    words = ["python", "java", "kotlin", "hangman", "computer"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    guessed_letters = set()
    attempts = 6

    print("\nWelcome to Hangman!")
    print("Guess the word:")

    # Game loop
    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        print("Attempts left:", attempts)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check if correct
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    # End of game
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
    else:
        print("\n💀 Game Over! The word was:", word_to_guess)


# ---------------- Main Loop ----------------
while True:
    play_hangman()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing Hangman! Goodbye 👋")
        break
