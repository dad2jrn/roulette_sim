# src/colors.py

def bet_on_black(spin_result):
    """Returns payout for betting on black."""
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    return 1 if spin_result in black_numbers else -1

def bet_on_red(spin_result):
    """Returns payout for betting on red."""
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    return 1 if spin_result in red_numbers else -1