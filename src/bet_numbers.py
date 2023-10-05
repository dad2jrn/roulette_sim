# src/bet_numbers.py

def bet_on_number(number, spin_result):
    """Returns payout for betting on a specific number."""
    return 35 if spin_result == number else -1