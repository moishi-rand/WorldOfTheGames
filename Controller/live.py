from Games import memory_game, guess_game, currency_roulette_game
from Utills import score
from Utills.utility import validate_input_int_number

#Return welcome str with name of player
def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG)." \
           f"\nHere you can find many cool games to play."

#Load game
def load_game():
    print(f"Please choose a game to play:"
          f"\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back."
          f"\n2. Guess Game - guess a number and see if you chose like the computer."
          f"\n3. Currency Roulette - Currency Roulette - try and guess the value of a random amount of USD in ILS.")
    game_number = validate_input_int_number(4)

    print("Please choose game difficulty from 1 to 5:")
    difficult_number = validate_input_int_number(6)
    is_win_game = False

    if(game_number == 1):
        is_win_game = memory_game.play(difficult_number)
    elif(game_number == 2):
        is_win_game = guess_game.play(difficult_number)
    elif (game_number == 3):
        is_win_game = currency_roulette_game.play(difficult_number)

    if(is_win_game):
        print("You Win!!!!!!!")
        update_player_score(difficult_number)
    else:
        print("Lose, try next time!")

def update_player_score(difficult):
    score.add_score(difficult)


