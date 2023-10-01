from pathlib import Path
import sys
import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).parent / 'src'))

from roulette import spin_wheel
from utils import determine_column, determine_dozen
from strategies import Fibonacci

def calculate_winnings(number, color):
    winnings = 0

    # Check for color (black)
    if color == "Black":
        winnings += 80  # Return the bet and the winnings

    # Check for column (2nd column)
    if determine_column(number) == "2nd":
        winnings += 30  # Return the bet and the winnings

    # Check for dozen (25-36)
    if determine_dozen(number) == "25-36":
        winnings += 30  # Return the bet and the winnings

    return winnings

def main():
    bankroll = 1000
    num_spins = int(input("Enter the number of spins you'd like to simulate: "))

    bankroll_history = [bankroll]

    for _ in range(num_spins):
        # The bet amount for black, 2nd column, and 3rd dozen
        total_bet = 60
        bankroll -= total_bet

        number, color = spin_wheel()
        winnings = calculate_winnings(number, color)
        bankroll += winnings

        print(f"Bet Amount: ${total_bet}")
        print(f"Wheel Result: {number} ({color})")
        print(f"Winnings: ${winnings}")
        print(f"Remaining Bankroll: ${bankroll}\n")

        bankroll_history.append(bankroll)

    # Plotting the bankroll progression
    plt.plot(bankroll_history)
    plt.title("Bankroll Progression Over Time")
    plt.xlabel("Number of Spins")
    plt.ylabel("Bankroll")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
