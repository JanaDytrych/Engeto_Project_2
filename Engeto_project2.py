import random

oddelovac = "-" * 60
print(f"Hello there!", "I've generated a random 4 digit number for you.", oddelovac, sep='\n')

input_tries = input("How many tries do you wanna get? (in range 1-30): ")
while True:
    if not str(input_tries).isdigit():
        input_tries = input("That is not a number, please try again: ")
    else:
        if int(input_tries) not in range(1, 31):
            input_tries = input("This is out of range, let's try again: ")
        else:
            print(oddelovac)
            break

print(f"""Let's play bulls and cows and start the game!
You have {input_tries} tries and I wish you a good luck.
{oddelovac}""")

def no_duplicate(num):
    if len(str(num)) == len(set(str(num))):
        return True
    else:
        return False

def generate_number():
    while True:
        number = random.randint(1000, 9999)
        if no_duplicate(number):
            return str(number)

def player_input_check(num):
    if num.isnumeric() == False:
        print("Yor can input only numbers! Please try again: ")
        return False
    elif len(num) != 4:
        print("Your number must have 4 digits, please try again: ")
        return False
    elif not no_duplicate(num):
        print("Sorry! No duplications allowed in your guess, let's try again: ")
        return False
    elif num.startswith(str("0")):
        print("Your number starts with 0 and that is not accepted, please enter your number again: ")
        return False
    return True

def bulls_cows_game(random, player):
    bull_cow = [0, 0]
    for index, number in zip(random, player):
        if number in str(random):
            if number == index:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

play_game = True
random_number = generate_number()
actual_tries = 0
input_tries = int(input_tries)

bull_string = ""
cow_string = ""

while play_game and input_tries > 0:
    # print("random number is ", random_number)
    player_guess = str(input("Enter a number: "))

    if player_input_check(player_guess) == False:
        continue
    print(f">>> {player_guess}")
    bull_cows = bulls_cows_game(random_number, player_guess)
    if bull_cows[0] == 1:
        bull_string = "bull"
    else:
        bull_string = "bulls"

    if bull_cows[1] == 1:
        cow_string = "cow"
    else:
        cow_string = "cows"
    print(f"{bull_cows[0]} {bull_string}, {bull_cows[1]} {cow_string}")

    input_tries -= 1
    actual_tries += 1
    if player_guess == random_number:
        play_game = False
        print(f"Congratulations! Your guess was right:) You needed {actual_tries} tries.")
        exit()
else:
    print(f"You lost! The number you were looking for is {random_number}. Maybe next time:)")
    play_game = False
