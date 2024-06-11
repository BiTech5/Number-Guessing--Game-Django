import random
def guess_fun(guess_nbr):
    nbr=random.randrange(1,10)
    if nbr == guess_nbr:
        return ('Your guess is correct')
    elif nbr>guess_nbr:
        return (f'Try a Bigger number than {guess_nbr}')
    elif nbr<guess_nbr:
        return (f'Try a Smaller number than {guess_nbr}')
    else:
        return ('Error')

