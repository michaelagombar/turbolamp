from random import randint
import sys

player_win_count = 0
computer_win_count = 0

def play():

    global player_win_count
    global computer_win_count

    dec = randint(1, 3)
    user_choice = input("Do you want (p)aper, (r)ock, or (s)cissors?")



    if user_choice == 'r':

        if dec == 1:
            print("Player selected ROCK, computer selected ROCK. DRAW!")
            score(player_win_count, computer_win_count)


        elif  dec == 2:
            print("Computer wins! Player selected ROCK, computer selected PAPER")
            computer_win_count += 1
            score(player_win_count, computer_win_count)


        elif dec == 3:
            print ("Player wins! Player selected ROCK, computer selected SCISSORS!")
            player_win_count += 1
            score(player_win_count, computer_win_count)

    if user_choice == 'p':

        if dec == 1:
            print("Player wins! Player selected PAPER, computer selected ROCK!")
            player_win_count += 1
            score(player_win_count, computer_win_count)

        elif dec == 2:
            print("DRAW! Player selected PAPER, computer selected PAPER!")
            score(player_win_count, computer_win_count)

        elif dec == 3:
            print("Computer wins! Player selected PAPER, computer selected SCISSORS!")
            computer_win_count += 1
            score(player_win_count, computer_win_count)

    if user_choice == 's':

        if dec == 1:
            print("Computer wins! Player selected SCISSORS, computer selected ROCK!")
            computer_win_count += 1
            score(player_win_count, computer_win_count)

        elif dec == 2:
            player_win_count += 1
            score(player_win_count, computer_win_count)


        elif dec == 3:
            print("DRAW! Player selected SCISSORS, computer selected SCISSORS!")
            score(player_win_count, computer_win_count)


def score(player_win_count, computer_win_count):
    print("Player score: {} Computer score:  {}".format(player_win_count, computer_win_count))
    play_again() #recursion overload issue



def play_again(): #this could be an issue moving forward, as I believe there could be a recursion overload.
    choice = input("Do you want to play again? y/n")
    if choice == 'y':
        play()
    else:
        print("OK! The final score was\n Player: {} to Computer: {}".format(player_win_count, computer_win_count))
        sys.exit()



play()