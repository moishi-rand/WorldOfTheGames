import random
from Utills.utility import validate_input_int_number


secret_number = 0
difficult_level = 0

#Return generated number between 1 to difficulty
def generate_number(difficulty):
    return random.randint(1, difficulty + 1)

#Return input number of user
def get_guess_from_user():
    print(f"Please guess the number from 1 to {difficult_level}")
    input_number = validate_input_int_number(difficult_level)
    return input_number

#Return if input of user equal to secret_number
def compare_results():
    return secret_number == get_guess_from_user()

#Start play the game, return if user win or not
def play(difficulty):
    global difficult_level
    difficult_level = difficulty
    global secret_number
    secret_number = 0
    secret_number = generate_number(difficult_level)
    return compare_results()

