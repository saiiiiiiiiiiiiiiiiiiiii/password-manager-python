# Technical Name
# Dice Rolling Turn-Based Game

# Description
# Developed a command-line dice rolling game in Python, 
# where 2 to 4 players take turns rolling a die to accumulate points. 
# Players must reach a target score of 50 points to win. 
# Implemented features include turn management, score tracking, and handling of special conditions 
# such as losing points on rolling a 1. Utilized random number generation and user input for interactive gameplay.

import random

def roll_dice():
    return random.randint(1, 6)

# Get the number of players
while True:
    players = input("Enter the number of players (between 2 and 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number.")

# Initialize scores
max_score = 50
players_score = [0 for _ in range(players)]

# Start the game
while max(players_score) < max_score:
    for i in range(players):
        print(f"\nPlayer {i + 1}'s turn:")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll? (y/n): ").lower()
            if should_roll != "y": 
                break
            else: 
                value = roll_dice()  
                if value == 1:
                    print("You rolled a 1. You lose your turn.")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value}. Your current score this turn is: {current_score}")

        players_score[i] += current_score
        print(f"Your total score is now: {players_score[i]}")

# Determine the winner
max_score = max(players_score)
winning_i = players_score.index(max_score)
print(f"\nPlayer {winning_i + 1} wins with a score of {max_score}!")
