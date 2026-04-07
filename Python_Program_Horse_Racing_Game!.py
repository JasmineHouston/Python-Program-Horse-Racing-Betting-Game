import random
import time

# Functions
def get_valid_bet(balance):
    """Gets a valid bet amount from user using control flow."""
    while True:
        try:
            bet = int(input(f"Enter your bet (1-{balance} chips): "))
            if 1 <= bet <= balance:
                return bet
            print("Invalid amount. Please try again.")
        except ValueError:
            print("Please enter a number.")

def run_race(horses):
    """Simulates a race by shuffling horse speeds."""
    print("\n...The horses are approaching the starting line...")
    time.sleep(1)
    print("...And they're off!")
    
    # Simulate racing progress
    for _ in range(3):
        time.sleep(0.5)
        print("...")

    # Store horse and their speed
    results = {horse: random.randint(1, 100) for horse in horses}
    
    # Sort horses by there descending speed
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    return sorted_results

def play_game():
    # Data Types & Setup
    # List of strings
    horses = ["Jasmine", "Grace", "Nova", "Stella"]
    balance = 20
    
    print("Welcome to the Python Program Horse Racing Betting Game!")
    
    # Control Flow - Main Game Loop 
    while balance > 0:
        print(f"\nYour current balance: {balance} chips")
        print("Horses:", ", ".join(horses))
        
        # User input
        player_horse = input("Choose your horse: ").capitalize()
        if player_horse not in horses:
            print("Invalid horse name.")
            continue
            
        bet = get_valid_bet(balance)
        
        # Run race
        results = run_race(horses)
        winner = results[0][0]
        
        # Control Flow - Outcome Assessment 
        print(f"\nWinner: {winner}!")
        
        if player_horse == winner:
            winnings = bet * 2
            balance += winnings
            print(f"Congratulations! You won {winnings} chips!")
        else:
            balance -= bet
            print(f"Sorry, {player_horse} lost. You lost {bet} chips.")
            
        if balance <= 0:
            print("Game Over! You are out of chips.")
            break
            
        if input("Play again? (y/n): ").lower() != 'y':
            break
            
    print("Thank you for playing!")

# Start the game
if __name__ == "__main__":
    play_game()
