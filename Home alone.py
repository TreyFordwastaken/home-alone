import random
import time

# Game Introduction
def print_intro():
    print("Welcome to Home Alone!")
    print("You're in your house, and burglars are coming.")
    print("Your goal is to set traps and prevent the burglars from breaking in.")
    print("You have a few rooms to choose from to set your traps.")
    print("Good luck!")

# Available rooms and traps
rooms = ["Living Room", "Kitchen", "Stairs", "Front Door", "Basement"]
traps = ["Paint Can Drop", "Marbles", "Nail Bed", "Icy Floor", "Blazing Hot Door Handle"]

# Player's setup
player_traps = []
player_rooms = []

# Burglars' arrival
def burglar_arrival():
    print("\nThe burglars are here!")
    time.sleep(2)
    print("They are trying to break in...")
    time.sleep(2)
    
    # Increase the chance of the burglars getting through if fewer traps are set
    trap_effectiveness = len(player_traps) * 0.1  # More traps = higher chance of success
    print(f"You have set {len(player_traps)} traps.")

    if random.random() < (0.5 + trap_effectiveness):
        print("The burglars encountered one of your traps!")
        print("They are defeated!")
        return True
    else:
        print("The burglars made it through!")
        return False

# Setting traps in rooms
def set_traps():
    print("\nYou need to set traps in rooms.")
    print("Choose a room from the following list:")
    for idx, room in enumerate(rooms):
        print(f"{idx + 1}. {room}")
    
    try:
        room_choice = int(input("Choose a room number to set a trap: ")) - 1
        if room_choice < 0 or room_choice >= len(rooms):
            print("Invalid room choice. Please try again.")
            return False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

    print("\nNow, choose a trap to set in this room:")
    for idx, trap in enumerate(traps):
        print(f"{idx + 1}. {trap}")
    
    try:
        trap_choice = int(input("Choose a trap number: ")) - 1
        if trap_choice < 0 or trap_choice >= len(traps):
            print("Invalid trap choice. Please try again.")
            return False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

    room = rooms[room_choice]
    trap = traps[trap_choice]
    
    # Ensure traps are not set in the same room twice
    if room in player_rooms:
        print(f"You've already set a trap in the {room}. Try another room.")
        return False

    player_rooms.append(room)
    player_traps.append(trap)
    print(f"You've set the {trap} in the {room}.\n")
    return True

# Game loop
def game():
    print_intro()
    
    # Set traps
    while len(player_rooms) < len(rooms):
        print(f"\nYou have {len(rooms) - len(player_rooms)} rooms left to set traps.")
        if not set_traps():
            continue
    
    # After setting all traps, burglars arrive
    print("\nAll traps have been set. Let's see if the burglars fall for them!")
    time.sleep(2)
    
    if burglar_arrival():
        print("\nYou successfully defended the house!")
    else:
        print("\nThe burglars got through your traps. They took everything!")
        print("Game Over.")

# Run the game
if __name__ == "__main__":
    game()
