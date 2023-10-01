# src/betting_strategies.py

class Fibonacci:

    def __init__(self, base_bet=1):
        self.fibonacci = [0, 1]
        self.index = 0
        self.base_bet = base_bet

    def next_bet(self, won_last=True):
        if won_last:
            self.index = max(0, self.index - 1)
        else:
            self.index += 1
            if self.index >= len(self.fibonacci):
                self.fibonacci.append(self.fibonacci[-1] + self.fibonacci[-2])
        return self.fibonacci[self.index] * self.base_bet


