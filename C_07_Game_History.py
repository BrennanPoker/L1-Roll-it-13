
# Initialise list to hold game history
game_history = []

# get date (base component does this already. code below fore testing purposes)


while True:
    rounds_played = input("Round?")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    comp_points = int(input("Computer points? "))
    winner = input("Who won?")
    user_score = int(input("User Score: "))
    comp_score = int(input("Computer Score: "))

    game_results = (f"Round: {rounds_played} User points {user_points} | " 
                   f"Computer Points {comp_points}, {winner} wins " 
                   f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)