import random

def play_round(player_choice, computer_choice):
    print(f"\nYour choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win this round!"
    else:
        return "Computer wins this round!"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = input("\nEnter your choice (rock/paper/scissors) or 'exit' to quit: ").lower()

        if player_choice == 'exit':
            print("Exiting the game. Goodbye!")
            break

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = play_round(player_choice, computer_choice)

        print(result)

if __name__ == "__main__":
    main()
≠
