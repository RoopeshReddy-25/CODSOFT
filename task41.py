import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    print(" Welcome to Rock-Paper-Scissors ")
    print("Instructions: Type rock, paper, or scissors to play.\n")

    while True:
        user_choice = input(" Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print(" Invalid choice, please try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"\n You chose: {user_choice}")
        print(f" Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!\n")
        elif result == "user":
            print(" You win!\n")
        else:
            print(" Computer wins!\n")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("\n Thanks for playing! Goodbye.")
            break
        print("-" * 40)

if __name__ == "__main__":
    main()
