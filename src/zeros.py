

def bet_on_zeros(zeros, spin_result):
    """Returns payout for betting on zeros (0 and/or 00 in American roulette)."""
    if zeros == 'both':
        return 35 if spin_result in [0, 37] else -1
    elif zeros == 0:
        return 35 if spin_result == 0 else -1
    elif zeros == 37:
        return 35 if spin_result == 37 else -1
    return -1