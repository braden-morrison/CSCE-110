# File: die_game.py
# Author: Braden Morrison
# Date: xx/xx/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu
# A program to play a Dice game.

import random


def roll_die():
    ''' Simulate a die roll '''
    return random.randint(1, 6)


def player_turn(player_name, other_player, player_score):
    '''
        Implements what happens on player's turn.
        Returns player's score, which represents
        the player's total score.
    '''
    option = 'r'
    print(f'\n*******{player_name}\'s turn********\n')

    # < Insert the rest of your code here. >
    while option == 'r':
        x1 = roll_die()
        x2 = roll_die()
        x3 = roll_die()
        player_score += x1 + x2 + x3
        if player_score > 18 and x1 != 2 and x2 != 2 and x3 != 2:
            print(f"Scores: {x1}, {x2}, and {x3}.")
            print(f"{player_name}'s score: {player_score} \n")
            break
            # switch turns
        else:
            print(f"Scores: {x1}, {x2}, and {x3}.")
            if x1 == 2 or x2 == 2 or x3 == 2:
                print(f"{player_name} got at least one 2.")
                player_score = 0
                print(f"{player_name}'s score: {player_score} ")
                input("Press <enter> to continue ...")
                break
                # switch turns
            print(f"{player_name}'s score: {player_score} \n")
            option = input("(p)ass or (r)oll? ")
            print()

    return player_score


def main():
    '''
        The main driver of the program. Call
        the player_turn() functions here.
    '''
    # make global variables for num of rolls for each player, update within function, check in main to see if even (maybe while loop until even)
    global name1
    global name2
    name1 = input("Enter the first player name: ")
    name2 = input("Enter the second player name: ")
    score1 = 0
    score2 = 0
    t1 = 0
    t2 = 0
    print()
    score1 = player_turn(name1, name2, score1)
    t1 = 1
    score2 = player_turn(name2, name1, score2)
    t2 = 1

    while score1 <= 18 and score2 <= 18:
        score1 = player_turn(name1, name2, score1)

        score2 = player_turn(name2, name1, score2)
        t2 += 2

    if score1 > 18 and score2 > 18:
        if score1 > score2:
            print(f"{name1} wins with a score of {score1}")
        elif score2 > score1:
            print(f"{name2} wins with a score of {score2}")
        else:
            print('Both players got the same score')
            print(f"{name1}: {score1} scores")
            print(f"{name2}: {score2} scores")
    elif score1 > 18 and score2 <= 18:
        print(f"{name1} wins with a score of {score1}")
    elif score2 > 18 and score1 <= 18:
        print(f"{name2} wins with a score of {score2}")


if __name__ == '__main__':
    main()
