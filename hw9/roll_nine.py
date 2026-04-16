import numpy as np
from math import floor

def play_the_game(r, n_games):
    
    """
    function simulates a game where 4 dice are rolled. if the player rolls a total less than 9 they get paid r dollars, otherwise they lose $1
    r: amount of money the player gets if they roll a total less than 9
    n_games: number of games played
    profit: total profit after playing n_games
    
    """

    # sets profit to 0 at the start of the game   
    profit = 0

    for i in range(n_games):
        rolls = np.random.randint(1, 7, 4)
        tot = sum(rolls)

        if tot < 9:
            profit += r
        else:
            profit -= 1
    
    avg_profit = profit / n_games
    return print(floor(avg_profit))

play_the_game(18.5, 100_000)
