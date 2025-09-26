import random

number_of_streaks = 0

for experiment_number in range(10000):
    flips = []
    cur_streak = 0

    for i in range(100):
        flip = 'H' if random.randint(0, 1) else 'T'
        flips.append(flip)
        cur_streak = cur_streak + 1 if flip == 'H' else 0

        if cur_streak == 6:
            number_of_streaks += 1

print('Chance of streak: %s%%' % (number_of_streaks / 100))