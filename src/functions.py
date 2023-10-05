# src/functions.py

from columns import bet_on_column
from colors import bet_on_red, bet_on_black
from bet_numbers import bet_on_number
from zeros  import bet_on_zeros
from dozens import bet_on_dozen



def resolve_bet_function(bet):
    if bet["type"] == "column":
        return lambda x: bet_on_column(bet["value"], x)
    elif bet["type"] == "color":
        if bet["value"] == "red":
            return bet_on_red
        elif bet["value"] == "black":
            return bet_on_black
    elif bet["type"] == "number":
        return lambda x: bet_on_number(bet["value"], x)
    elif bet["type"] == "zeros":
        return lambda x: bet_on_zeros(bet["value"], x)
    elif bet["type"] == "dozen":  # Added condition for 'dozen'
        return lambda x: bet_on_dozen(bet["value"], x)
    else:
        raise ValueError(f"Unknown bet type: {bet['type']}")