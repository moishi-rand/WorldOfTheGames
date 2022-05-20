
#Update score of the player
def add_score(difficulty):
    points_of_winning = difficulty * 3 + 5

    try:
        score_file = open("my_text.txt", "r")
        points_of_winning += int(score_file.read())
        score_file = open("my_text.txt", "w")
    except:
        score_file = open("my_text.txt", "w+")
    finally:
        score_file.write(f"{points_of_winning}")
        score_file.close()
