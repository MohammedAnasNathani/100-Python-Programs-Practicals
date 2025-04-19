import random

# Board setup
snake_and_ladder = {2: 15, 7: 29, 8: 11, 16: 3, 21: 42, 28: 84, 36: 44, 47: 26, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91, 80: 100}
position = 0

# Game loop
while position < 100:
    roll = random.randint(1, 6)
    print(f"Rolled: {roll}")
    position += roll
    
    # Check if the player hits a snake or ladder
    if position in snake_and_ladder:
        print(f"Hit a snake or ladder! Moving to {snake_and_ladder[position]}")
        position = snake_and_ladder[position]

    print(f"Current position: {position}")
    
    if position >= 100:
        print("Congratulations! You reached 100.")
        break
