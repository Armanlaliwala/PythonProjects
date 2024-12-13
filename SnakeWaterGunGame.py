import random

choices = ["S", "W", "G"]
computer = random.choice(choices)  # Get the shorthand version (S, W, G)

player = input("Player Input - Snake = (S), Water = (W), Gun = (G): ").strip().upper()
print(f"Player: {player}")
print(f"Computer: {computer}")

if player not in ['S', 'W', 'G']:
    print("Invalid Input")
elif player == computer:
    print("Draw")
elif (player == 'G' and computer == 'S') or (player == 'S' and computer == 'W') or (player == 'W' and computer == 'G'):
    print("User Win")
else:
    print("Computer Win")
