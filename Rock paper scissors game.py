import random

print("🎮 Welcome to Rock, Paper, Scissors Game!")

# Initialize scores
user_score = 0
computer_score = 0

# Define possible choices
choices = ["rock", "paper", "scissors"]

while True:
    # User input
    user_choice = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()
    
    if user_choice == 'q':
        print("\nThanks for playing!")
        print(f"Final Score ➤ You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in choices:
        print("❗ Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Computer random choice
    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {computer_choice}")

    # Determine result
    if user_choice == computer_choice:
        print("⚖️ It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ You lose this round.")
        computer_score += 1

    # Show current score
    print(f"🔢 Score ➤ You: {user_score} | Computer: {computer_score}")
