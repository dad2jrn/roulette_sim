# src/plot.py


import matplotlib as mpl
import matplotlib.pyplot as plt

# Setting up for better font rendering in plots
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14


def plot_bankroll_and_bet(bankroll_history, bet_history):
    """Plot the bankroll and bet amount over spins."""
    fig, ax1 = plt.subplots(figsize=(10,6))

    color = 'tab:blue'
    ax1.set_xlabel('Spins')
    ax1.set_ylabel('Bankroll', color=color)
    ax1.plot(bankroll_history, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Bet Amount', color=color)
    ax2.plot(bet_history, color=color, linestyle='--')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Bankroll and Bet Amount Over Time')
    plt.grid(True)
    plt.show()