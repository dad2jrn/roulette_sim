# src/custombets.py

from .roulette_wheel import spin_roulette

def simulate_custom_bets(bet_functions, bet_amounts, spins, initial_bankroll):
    bankroll = initial_bankroll
    for _ in range(spins):
        spin_result = spin_roulette()
        for func, amount in zip(bet_functions, bet_amounts):
            bankroll += func(spin_result) * amount
    return bankroll