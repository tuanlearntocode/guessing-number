from random import randint

# generate number

def generate_number():
    program_number = randint(1,100)
    return program_number

# user input

def user_input():

    condition = True
    number = 0

    while condition:
        number = input('Your number is: ')
        if number.isdigit() == True:
            condition = False
        else:
            print('Invalid number, try again!')
    return int(number)

# check number

def check_number(guess, program_number):
    check = True
    if guess > program_number:
        print('Your number is bigger than mine')
    elif guess < program_number:
        print('Your number is smaller than mine')
    else:
        print('You got the right answer')
        check = False
    return check

# game_on

def game_on():
    program_number = generate_number()
    game_continue = True
    while game_continue:
        guess = user_input()
        game_continue = check_number(guess, program_number)

game_on()

