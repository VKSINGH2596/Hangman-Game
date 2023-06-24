import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f"************ {hangman_art.logo} *************\n")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"\nWord: {' '.join(display)}")
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"\nThe letter '{guess}' is already entered, try a different one!")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"\nThe letter '{guess}' is not present in the word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    print(f"{hangman_art.stages[lives]}\n")

if lives == 0:
    choice = input("\nDo you wanna know what the word was? (Y/N): ").upper()
    if choice == "Y":
        print(f"The word was '{chosen_word}'.")
        print("\n***************** Thanks for Playing! *****************")
    else:
        print("\n***************** Thanks for Playing! *****************")

else:
    print("\n*****************Thanks for Playing!!*****************")
