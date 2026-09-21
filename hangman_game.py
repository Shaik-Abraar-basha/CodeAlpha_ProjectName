import random

words = ["python", "computer", "program", "coding", "developer"]

word = random.choice(words)
guessed_word = "_" * len(word)
incorrect_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < 6 and "_" in guessed_word:
    print("\nWord:", guessed_word)
    guess = input("Enter a letter: ").lower()

    if guess in word:
        new_word = ""

        for i in range(len(word)):
            if word[i] == guess:
                new_word += guess
            else:
                new_word += guessed_word[i]

        guessed_word = new_word
        print("Correct guess!")

    else:
        incorrect_guesses += 1
        print("Incorrect guess!")
        print("Incorrect guesses:", incorrect_guesses)

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)