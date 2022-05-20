import random
from tkinter import *
from utility import validate_input_list_numbers

limit_range = 101
list_numbers = []
difficult_level = 0
time_for_display_numbers_on_screen = 2000

#Generate a list of random numbers between 1 to 101.
def generate_sequence(difficulty):
    for i in range(difficulty):
        list_numbers.append(random.randint(1, limit_range))

#Display list numbers for user on limited time
def display_list_numbers_to_user():
    list_numbers_text = f"This list of numbers for remember: {list_numbers}"
    root = Tk()
    Message(root, text=list_numbers_text, padx=100, pady=100).pack()
    root.after(time_for_display_numbers_on_screen, root.destroy)
    root.mainloop()

#Get input of list number from user
def get_list_from_user(difficulty):
    list_numbers_user = validate_input_list_numbers(difficulty)
    return list_numbers_user

##Return if list number of user equal to list_numbers
def is_list_equal():
    return list_numbers == get_list_from_user(len(list_numbers))

#Start play the game, return if user win or not
def play(difficulty):
    list_numbers.clear()
    global difficult_level
    difficult_level = difficulty
    generate_sequence(difficult_level)
    display_list_numbers_to_user()
    return is_list_equal()







