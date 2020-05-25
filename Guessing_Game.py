import random

def f1():
    computers_number = random.randint(1,100)
    prompt = "I have thought of a number. Take a guess. "

    while True:
        players_guess = input(prompt)
        if computers_number == int(players_guess):
            print("Well done! ")
            break
        elif computers_number > int(players_guess):
            print("Too low. ")
        else:
           print("Too high. ")
        prompt = "Guess again. "

def f2():
    while True:
        f1()
        prompt = "Do you want to try again? n/Y "
        players_input = input(prompt)
        if players_input == "Y":
            pass
        else:
            print("Thank you for playing!" )
            break

# ------- main
f2()