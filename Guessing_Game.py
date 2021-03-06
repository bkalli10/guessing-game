import random
import csv
from pprint import pprint
from datetime import datetime
import shutil


# import pickle
# RESULT_FILE="result.txt"
# RESULT_MAP={}
# RESULT_MAP[person_name] = score
# pickle.dump(RESULT_MAP, open(RESULT_FILE, 'wb'))
# result2 = pickle.load(open(RESULT_FILE, 'rb'))

# RESULT_MAP={}
SCORE_FILE="score.csv"
SCORE_DATA=[]

NOW = datetime.now()
# date_string = now.strftime("%Y-%m-%dT%H:%M:%S")
NOW_STRING = NOW.isoformat('T', 'seconds')

# --------- functions


def f_main():
    global SCORE_DATA
    SCORE_DATA = f_read_csv_file()
    print("-------------------------------------------------------------------------------------------------------")
    print("Welcome to the GREAT GUESSING GAME! ")
    print("You have been chosen to use your cunning and wit to deduce the MAGIC NUMBER!!!")
    print("Continue IF YOU DARE. . . . .")
    print("-------------------------------------------------------------------------------------------------------")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("-------- INSTRUCTIONS --------")
    print("To begin the game, type your name when Gerald asks for it and hit enter.")
    print("To exit the game while the game is still in action, type stop and hit enter.")
    print("")
    player_name = f_get_name()
    f_want_to_play_again(player_name)

    pprint(SCORE_DATA)
    f_write_csv_file()
    shutil.copy(SCORE_FILE, "logs/"+SCORE_FILE + "." + NOW_STRING)

    f_print_ranking()


def f_get_name():
    name_prompt = "What is your name? "
    player_name = input(name_prompt)
    return player_name


def f_playing_game(player_name):
    computers_number = random.randint(1, 100)
    prompt = "I have thought of a number, " + player_name + ". Take a guess. "
    score = 0

    while True:
        players_guess = input(prompt)
        player_wants_to_stop = 'stop'
        score = score + 1
        if player_wants_to_stop == players_guess:
            are_you_sure_prompt = "Are you sure you want to exit the game? n/y "
            player_confirmation = input(are_you_sure_prompt)
            if player_confirmation == "y":
                break
            else:
                pass
        elif computers_number == int(players_guess):
            print("Well done, " + player_name + "! ")
            row = (player_name, NOW_STRING, score)
            SCORE_DATA.append(row)
            break
        elif computers_number > int(players_guess):
            prompt = "Too low. Guess again. "

        else:
            prompt = "Too high. Guess again. "


    # RESULT_MAP[player_name] = score
    # print("Your score is " + str(score))


def f_want_to_play_again(player_name):
    while True:
        f_playing_game(player_name)
        prompt = "Do you want to play again? n/y "
        players_input = input(prompt)
        if players_input == "y":
            ending_prompt = "Great! Is this still " + player_name + " playing the game? n/y "
            new_player_prompt = input(ending_prompt)
            if new_player_prompt == "y":
                print("Welcome back! Thanks for playing again!")
            else:
                player_name = f_get_name()

        else:
            print("Thank you for playing," + player_name + "!")
            break


def f_read_csv_file():
    print("function f_read_csv_file ...")
    data = []
    with open(SCORE_FILE) as f:
        reader = csv.reader(f)
        # data = list(map(tuple, reader))
        for (name, date, score) in reader:
            row=(name, date.strip(), int(score))
            data.append(row)
    return data

def f_write_csv_file():
    print ("function f_write_csv_file ...")
    with open(SCORE_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(SCORE_DATA)

def f_print_ranking():
    print ("function f_print_ranking ...")
    print("")
    print("")

    # sort data by name
    data1 = sorted(SCORE_DATA, key=lambda x: (x[0]))

    # minScore, name, gamesPlayed, totalScore, avgScore
    data2=[]
    prev_name=''
    data_counter=0
    minScore=1000000
    for (name, date, score) in data1:
        data_counter=data_counter+1
        if data_counter > 1 and prev_name != name:
            row=(minScore, prev_name)
            data2.append(row)
            minScore = 1000000
        prev_name = name
        if score < minScore:
            minScore = score

    row=(minScore, prev_name)
    data2.append(row)

    # sort data by score
    data3 = sorted(data2, key=lambda x: (x[0], x[1]))

    rank = 1
    display_rank = 0
    prev_score = 0
    print("  rank  score   name")
    print("  ----  -----   ----")
    for (score, name) in data3:
        if score != prev_score:
            display_rank = display_rank + 1
        print (" %4d %5d     %s" % (display_rank, score, name))
        prev_score = score
        rank = rank + 1

# --------------------------------------
if __name__ == "__main__":
    f_main()
