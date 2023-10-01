# src/roulette.py

import random

NUMBERS = list(range(37))
COLORS = ["Green", "Red", "Black", "Red", "Black", "Red", "Black", "Red", "Black", "Red",
        "Black", "Black", "Red", "Black", "Red", "Black", "Red", "Black", "Red", "Red",
        "Black", "Red", "Black", "Red", "Black", "Red", "Black", "Red", "Black", "Black",
        "Red", "Black", "Red", "Black", "Red", "Black", "Red"]

def spin_wheel():
    result = random.choice(NUMBERS)
    return result, COLORS[result]

if __name__ == "__main__":
    print(spin_wheel())