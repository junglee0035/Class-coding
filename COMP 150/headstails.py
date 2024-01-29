def flip():
    import random
    coinflip = random.randrange(2)
    if coinflip == 0:
        print('Heads')
    else:
        print('Tails')

flip()