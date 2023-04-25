import random
from hangman_words import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

end_of_game = False
user_lives = 6
print(logo)

# Testing code.
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks in list for each letter in the chosen word.
display_list = []
for _ in range(word_len):
    display_list.append("_")

# Game starts.
while not end_of_game:
    user_guess = input("Please guess a letter: ").lower()

    # If the user has entered a letter they've already guessed,
    # print the letter and let them know.
    if user_guess in display_list:
        print(f"You've already guessed letter: {user_guess}")

    # Check guessed letter in chosen word.
    for position in range(word_len):
        char = chosen_word[position]
        if char == user_guess:
            display_list[position] = char

    # Check if the user guess is wrong.
    # If the letter is not in the chosen_word, print out the letter
    # and let them know it's not in the word.
    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        user_lives -= 1
        if user_lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display_list)}")

    # Check if user has correctly guessed all letters.
    if "_" not in display_list:
        end_of_game = True
        print("You win!")

    print(stages[user_lives])
