class CustomFibonacciStrategy:
    def __init__(self):
        self.base_bets = {'black': 40, '2nd_column': 10, '3rd_dozen': 10}
        self.current_index = 0  # Start at the first index of the Fibonacci sequence
        self.previous_outcome = "win"

    def calculate_bet(self, outcome):
        if outcome == "win":
            self.current_index = 0  # Reset the Fibonacci sequence index on a win
        elif self.previous_outcome == "loss":
            self.current_index += 1  # Move to the next number in the sequence on a loss

        self.previous_outcome = outcome

        # Calculate the Fibonacci multiplier
        multiplier = self._fibonacci(self.current_index)

        # Return bets scaled by the Fibonacci multiplier
        return {k: v * multiplier for k, v in self.base_bets.items()}

    def _fibonacci(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a



