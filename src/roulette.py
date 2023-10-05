# src/roulette.py

from .roulette_wheel import spin_roulette
from .fibonacci import fibonacci

def roulette(initial_bet, max_spins, initial_bankroll):
    """Simulate the betting strategy on American roulette."""
    bankroll = initial_bankroll
    bankroll_history = [bankroll]
    bet_history = [initial_bet]

    bet_amount = initial_bet
    consecutive_losses = 1

    for spin in range(max_spins):
        result = spin_roulette()
        fib_value = fibonacci(consecutive_losses)

        if result == 'BLACK':
            print(f"Spin {spin+1}: Bet: ${bet_amount}({fib_value}). Result: WIN.")
            bankroll += bet_amount
            consecutive_losses = max(1, consecutive_losses - 2)  # Move back two steps in Fibonacci sequence
            bet_amount = initial_bet * fibonacci(consecutive_losses)
        else:
            print(f"Spin {spin+1}: Bet: ${bet_amount}({fib_value}). Result: LOSS.")
            bankroll -= bet_amount
            consecutive_losses += 1
            bet_amount = initial_bet * fibonacci(consecutive_losses)

        # If bankroll is exhausted, break from the loop
        if bankroll <= 0:
            bankroll = 0
            bankroll_history.append(bankroll)
            bet_history.append(0)
            break

        bankroll_history.append(bankroll)
        bet_history.append(bet_amount)

    return bankroll_history, bet_history