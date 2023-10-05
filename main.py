# /main.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

# import local library
from plot import plot_bankroll_and_bet
from userbets import simulate_with_user_bets


# Sample usage:
bets = [
    # {"type": "column", "value": 1, "amount": 5}, #  <-- 1rd Column (player row)
    # {"type": "column", "value": 2, "amount": 5}, #  <-- 2rd Column (middle row)
    # {"type": "column", "value": 3, "amount": 5}, #  <-- 3rd Column (dealer row)
    # {"type": "dozen", "value": 1, "amount": 5}, #  <-- 1rd Dozen (1 - 12)
    # {"type": "dozen", "value": 2, "amount": 5}, #  <-- 2rd Dozen (13 - 24)
    {"type": "dozen", "value": 3, "amount": 5}, #  <-- 3rd Dozen (25 - 36)
    # {"type": "color", "value": "red", "amount": 5},
    # {"type": "color", "value": "black", "amount": 10},
    # {"type": "zeros", "amount": 5}
]
spins = 200 # <-- total number of spins to test
initial_bankroll = 1000 # <-- Your starting bankroll each run

final_bankroll, bankroll_history, bet_history = simulate_with_user_bets(
    bets, spins, initial_bankroll
)
print(f"Final bankroll after {spins} spins: ${final_bankroll}")

# Plotting
plot_bankroll_and_bet(bankroll_history, bet_history)
