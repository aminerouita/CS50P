# This script recommends games based on difficulty and player type
# Prompt user for difficulty and player type make sure inputs are valid

def main():
    difficulty = input("Enter the difficulty level (Chill, Casual, Hard) : ").strip().capitalize()

    if difficulty not in ["Chill", "Casual", "Hard"]:
            difficulty = input(difficulty + " is not a difficulty level. Please enter Chill, Casual, or Hard: ").strip().capitalize()
    else:
        print("You have selected " + difficulty + " as difficulty.")

    
    players = input("Multiplayer or Singleplayer? (m/s): ").strip().capitalize()
    
    if players not in ["M" , "S"]:
            players = input(players + " is not a game mode. Please enter M for Multiplayer or S for Singleplayer. ").strip().capitalize()
    elif players == "M" :
         print("You have selected Multiplayer mode.")
    else:
        print("So going solo? Good for you.")
    
    # Call the recommend function with the inputs

    recommend(difficulty, players)

 # recommend based on inputs

def recommend(difficulty, players):
    print(f"Recommended games based on your choices of {difficulty} and {players} is:")
    if difficulty == "Chill" and players == "M":
        print("Stardew Valley")
    elif difficulty == "Chill" and players == "S":
        print("Animal Crossing")
    elif difficulty == "Casual" and players == "M":
        print("Mario Kart")
    elif difficulty == "Casual" and players == "S":
        print("Overcooked")
    elif difficulty == "Hard" and players == "M":
        print("Sekiro")
    elif difficulty == "Hard" and players == "S":
        print("Dark Souls")
    else:
        print("We coudn't do it. Your taste is quite unique! Go look for it yourself.")

main()


