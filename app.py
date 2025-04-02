import random

def get_user_choice():
    print("Enter your choice: rock, paper, or scissors")
    choice = input("Your choice: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0  # Initialize player's score
    total_rounds = 0  # Initialize total rounds
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")  # Ensure the result is clearly labeled
        
        total_rounds += 1  # Increment total rounds
        if result == "You win!":
            player_score += 1  # Increment score for a win
        
        while True:  # Loop until valid input is provided
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid input. Please type 'yes' or 'no'.")
        
        if play_again != "yes":
            print(f"Thanks for playing! Your final score is: {player_score}, Total rounds played: {total_rounds}")  # Display final stats
            break

if __name__ == "__main__":
    play_game()