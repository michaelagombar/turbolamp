import random
def guess_number():
    current_guess = 0
    my_number = randrange(1,20)

    name = input("Hello! What's your name?" )
    print("Cool! Nice to meet you " + name + " let's see if you can guess my number!")

    while current_guess < 5:
        print("guess a number between 1 and 20!")
        guess = input()
        guess = int(guess)
        current_guess += 1

        if guess < my_number:3
           print("Nope! My number is higher! Guess again!")
        elif guess > my_number:
            print("Nope! My number is lower! Guess again!")
        elif guess == my_number:
            break
    if guess == my_number:
        print("You're a  genius " + name + " and it only took " + current_guess +" times!")
    if guess != my_number:
        print("No! My number was: " + my_number)