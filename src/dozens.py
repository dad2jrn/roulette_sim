# src/dozens.py

def bet_on_dozen(dozen, spin_result):
    """Returns payout for betting on a specific dozen."""
    if dozen == 1 and spin_result in range(1, 13):
        return 2
    elif dozen == 2 and spin_result in range(13, 25):
        return 2
    elif dozen == 3 and spin_result in range(25, 37):
        return 2
    return -1

