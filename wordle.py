
import numpy as np
import random
import wordle_lists
import pygame


def retrieve_random_word():
    word_list = wordle_lists.WORDS
    word = random.choice(word_list)
    word = word.upper()
    return word


def does_guess_qualify(user_guess):
    if len(user_guess) != 5:
        return False
    else:
        qual_score = 0
        for letter in user_guess:
            try:
                q = wordle_lists.LEGAL_CHARACTERS.index(letter.lower())
                qual_score += 1
            except ValueError:
                qual_score += 0

        if qual_score == 5:
            return True
        else:
            return False


def letter_in_word(_list, char):
    try:
        _list.index(char)
        return True
    except ValueError:
        return False


# list1 is the guess_list. list2 is the word_list
def letter_in_position(list1, list2, position):
    guess_pos = list1[position]
    word_pos = list2[position]
    if guess_pos == word_pos:
        return True
    else:
        return False


# There will be a bug if the guess has the same letter in it twice
# list1 is guess_list. list2 is letter_list
def get_character_value(list1, list2, character):
    z = list1.index(character)
    if letter_in_word(list2, character) is True and letter_in_position(list1, list2, z) is True:
        return 2
    elif letter_in_word(list2, character) is True:
        return 1
    else:
        return 0


def show_results(array_name):
    for array_list in array_name:
        print(array_list)


#def results_to_json():


def is_guess_correct(list1):
    unique_values = np.unique(list1)
    num_unique_values = len(unique_values)
    unique_val = int(unique_values[0])

    if num_unique_values == 1 and unique_val == 2:
        return True
    else:
        return False


def play_game():
    word = retrieve_random_word()
    guess_count = 0
    print("""
Thank you for playing wordle. The purpose of this game is guess a 5-letter word from scratch.
The only information you are given is based off of your own guesses.
---------------------------------------------------------------------------------------------"
Here is what you need to know regarding the output:
    0 - the guessed letter is not in the word
    1 - the guessed letter is in the word, but in the wrong position
    2 - the guessed letter is in the word and in the correct position
---------------------------------------------------------------------------------------------
    """)
    letter_list = []
    for letter in word:
        letter_list.append(letter)

    while guess_count < 5:
        if guess_count == 0:
            print("This is your first guess. You have 5 remaining.")
        elif guess_count == 1:
            print("This is your second guess. You have 4 remaining.")
        elif guess_count == 2:
            print("This is your third guess. You have 3 remaining.")
        elif guess_count == 3:
            print("This is your fourth guess. You have 2 remaining.")
        elif guess_count == 4:
            print("This is your final guess. Good luck!!!")

        user_guess = input("guess > ").upper()
        while not does_guess_qualify(user_guess):
            print("I'm sorry, your guess must be 5 characters. Numbers and symbols are not allowed.")
            user_guess = input("guess > ").upper()

        guess_count += 1
        guess_list = []

        for guess_letter in user_guess:
            guess_list.append(guess_letter)

        results = []

        for guess_letter in user_guess:
            results.append(get_character_value(guess_list, letter_list, guess_letter))

        resultstemp = [guess_list], [results]
        results_array = np.array(resultstemp)

        show_results(results_array)

        if is_guess_correct(results_array[1]) is True:
            game_over = True
            print("Congrats!! You've guessed the word!!!")
            break

    if game_over is True:
        print("||| GAME OVER |||")
        print(f"Sorry, the word you were looking for was: {word}")

    print("""--------------------------------------------------------------
Thank you for playing
--------------------------------------------------------------""")


play_game()