import random  # random number generator

def roll():
    min_val = 1
    max_val = 6
    roll_value = random.randint(min_val, max_val)
    return roll_value

# Getting the number of players
while True:  # check valid number
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)  # valid number of players
        if 1 <= players <= 4:
            break
        else:
            print("Invalid selection. Select a number between 1 and 4.")
    else:
        print("Invalid input. Please enter a number.")

print(f"Number of players: {players}")

# Initialize player scores
max_score = 50
player_scores = [0] * players  # list of individual scores
print(f"Initial player scores: {player_scores}")

# Loop until someone reaches the max score
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn. Current score: {player_scores[player_idx]}")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_scores = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ")
            if should_roll.lower() == 'n':
                break
            elif should_roll.lower() != 'y':
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

            value = roll()
            print(f"You rolled a {value}")

            if value == 1:
                print("Rolled a one, your turn is over.")
                current_scores = 0
                break
            else:
                current_scores += value
                print(f"Your current turn score is {current_scores}")

        player_scores[player_idx] += current_scores
        print(f"Player {player_idx + 1}'s total score is now {player_scores[player_idx]}")

        # Check if this player has won
        if player_scores[player_idx] >= max_score:
            print(f"\nPlayer {player_idx + 1} wins with a score of {player_scores[player_idx]}!")
            break

max_score == max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player Number", winning_idx + 1, "is the winner with score of:", max_score)
