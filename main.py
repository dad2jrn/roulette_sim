from pathlib import Path
import sys
import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).parent / 'src'))

from roulette import spin_wheel
from utils import determine_column, determine_dozen
from strategies import CustomFibonacciStrategy

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_winnings(number, color, bet_amounts):
    winnings = 0
    if color == "Black":
        winnings += bet_amounts['black'] * 2
    if determine_column(number) == "2nd":
        winnings += bet_amounts['2nd_column'] * 3
    if determine_dozen(number) == "25-36":
        winnings += bet_amounts['3rd_dozen'] * 3
    return winnings


def main():
    bankroll = 1500
    num_spins = int(input("Enter the number of spins you'd like to simulate: "))

    strategy = CustomFibonacciStrategy()

    bankroll_history = [bankroll]

    for _ in range(num_spins):
        number, color = spin_wheel()

        bet_amounts = strategy.calculate_bet(None)  # Initial call to get the base bets
        total_bet = sum(bet_amounts.values())

        winnings = calculate_winnings(number, color, bet_amounts)

        # Determine outcome of the spin
        outcome = "win" if winnings > total_bet else "loss"

        # Update strategy with outcome
        strategy.calculate_bet(outcome)

        bankroll -= total_bet
        bankroll += winnings

        print(f"Bet Amounts: {bet_amounts}")
        print(f"Total Bet: ${total_bet}")
        print(f"Wheel Result: {number} ({color})")
        print(f"Winnings: ${winnings}")
        print(f"Remaining Bankroll: ${bankroll}\n")

        bankroll_history.append(bankroll)


if __name__ == "__main__":
    main()
    exit()
