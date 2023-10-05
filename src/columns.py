# src/columns.py

def bet_on_column(column, spin_result):
    """Returns payout for betting on a specific column."""
    if column == 1 and spin_result in range(1, 34, 3):
        return 2
    elif column == 2 and spin_result in range(2, 35, 3):
        return 2
    elif column == 3 and spin_result in range(3, 36, 3):
        return 2
    return -1