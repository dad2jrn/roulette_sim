# src/userbets.py

from fibonacci import fibonacci
from functions import resolve_bet_function
from roulette_wheel import spin_roulette

def simulate_with_user_bets(bets, spins, initial_bankroll):
    bet_functions = [resolve_bet_function(bet) for bet in bets]
    bet_amounts = [bet["amount"] for bet in bets]

    bankroll = initial_bankroll
    bankroll_history = [bankroll]
    bet_history = []

    consecutive_losses = 1  # Track consecutive losses for the Fibonacci sequence

    for spin in range(spins):
        spin_result = spin_roulette()
        total_bet = 0
        winnings = 0

        fib_value = fibonacci(consecutive_losses)
        bet_for_this_spin = fib_value * bet_amounts[0]  # Assuming all bets are of the same base amount for simplicity

        for func, amount in zip(bet_functions, bet_amounts):
            outcome = func(spin_result)
            bankroll += outcome * amount
            winnings += outcome * amount
            total_bet += amount if outcome < 0 else 0  # Only adding up lost amounts

        if winnings < 0:
            print(f"Spin {spin+1}: Bet: ${bet_for_this_spin}({fib_value}). Result: LOSS.")
            consecutive_losses += 1
        else:
            print(f"Spin {spin+1}: Bet: ${bet_for_this_spin}({fib_value}). Result: WIN.")
            consecutive_losses = max(1, consecutive_losses - 2)

        bankroll_history.append(bankroll)
        bet_history.append(bet_for_this_spin)

    return bankroll, bankroll_history, bet_history