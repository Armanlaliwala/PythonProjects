import random

# Choices for the game
choices = ["S", "W", "G"]  # S: Snake, W: Water, G: Gun

# Results matrix using a dictionary
results = {
    ('S', 'S'): "Draw",
    ('W', 'W'): "Draw",
    ('G', 'G'): "Draw",
    ('G', 'S'): "User Win",
    ('S', 'W'): "User Win",
    ('W', 'G'): "User Win",
    ('S', 'G'): "Computer Win",
    ('W', 'S'): "Computer Win",
    ('G', 'W'): "Computer Win"
}

# Randomly select a choice for the computer
computer = random.choice(choices)

# Get the player's input, remove any surrounding whitespace, and convert it to uppercase
player = input("Player Input - Snake(S), Water(W), Gun(G): ").strip().upper()

# Display player's and computer's choices
print(f"Player: {player}")
print(f"Computer: {computer}")

# Check for invalid input
if player not in choices:
    print("Invalid Input")
else:
    # Determine the result using the results dictionary
    result = results[(player, computer)]
    print(result)
