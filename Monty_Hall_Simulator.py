import random

# https://en.wikipedia.org/wiki/Monty_Hall_problem
# Suppose you're on a game show, and you're given the choice of three doors: 
# Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host,
# who knows what's behind the doors, opens another door, say No. 3, which has a goat.
# He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

total_rounds = 1000000

# Inititate rewards list and win record
choices = ['goat', 'goat', 'car']
win_record_if_player_switches = 0
win_record_if_player_does_not_switch = 0

for round in range(total_rounds):
    # Shuffle rewards
    random.shuffle(choices)
    # By default, player will pick the first choice
    # The host will now open one of the remaining doors to reveal the goat
    # The player can choose to switch to the not-yet revealed door or not
    if choices[1] == 'goat':
        if choices[2] == 'car':
            win_record_if_player_switches += 1
        else:
            win_record_if_player_does_not_switch += 1
    elif choices[2] == 'goat':
        if choices[1] == 'car':
            win_record_if_player_switches += 1
        else:
            win_record_if_player_does_not_switch += 1

print('Simulation done over', total_rounds, 'rounds.')
print('If the player switched their choice after one of the remaining door is revealed to be a goat, '
      'they would have won', win_record_if_player_switches, 'times.')
print('If they did not switch, they would have won', win_record_if_player_does_not_switch, 'times.')
