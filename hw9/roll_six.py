import numpy as np

def roll_the_die(n_dice, n_experiments):
    
    """
    function estimates the probability of getting at least one 6 when rolling n dice.

    n_dice: number of dice rolled for each experiment
    n_experiments: number of experiments performed
    probability: probability of getting at least one 6 

    """

    ct = 0 
    rolls = []
    
    # simulates rolling n dice n times and saves the rolls in a list
    for i in range(n_experiments):
        roll = np.random.randint(1, 7, n_dice)
        rolls.append(roll)
    print(rolls)
    # checks each roll for a 6 and adds to the count if one is found
    for roll in rolls: 
        if 6 in roll:
            ct+=1

    probability = ct / n_experiments

    return probability


# roll_the_die(4, 1000)