import random #importing random module

while True: #iterate loop
    user_action = input("Enter a choice (rock, paper, scissors): ") #take input
    possible_actions = ["rock", "paper", "scissors"]
    #using random function
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") #display both output what is selected by you and computer
    
    
#conditions to check who won the game
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes sissors! You lose.")
        else:
            print("Paper covers rock! you lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! Yu win!.")
        else:
            print("scissors cut paper! you lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper! You win.")
        else:
            print("rock smashes scissors! you lose.")
    #take input for playing  agin
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break