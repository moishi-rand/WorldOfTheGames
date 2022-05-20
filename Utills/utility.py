#Help functions and variables
import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

#A function to clear the screen
def screen_cleaner():
    os.system('cls')

#Validate the input is int number and number in range
def validate_input_int_number(validate_range):
    while True:
        try:
            input_number = int(input())
            if input_number not in range(1, validate_range):
                print(f"Please, enter only integer between 1 and {validate_range - 1}")
                continue
        except ValueError:
            print(f"Please, enter only integer between 1 and {validate_range - 1}")
            continue
        else:
            return input_number
            break

#Validate the input is float number
def validate_input_number():
    while True:
        try:
            input_number = float(input())
        except ValueError:
            print("Please, enter only float number")
            continue
        else:
            return input_number
            break

#Validate the input of list numbers from user
def validate_input_list_numbers(list_size):
    while True:
        try:
            list_numbers = list(map(int, input("Enter list numbers: ").split()))
            if len(list_numbers) != list_size:
                print(f"Please enter the exact {list_size} of numbers")
                continue
        except ValueError:
            print(f"Please, enter only integers to list")
            continue
        else:
            return list_numbers
            break
