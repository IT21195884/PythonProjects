import random


def guessUser(x):
    guess = random.randint(1,x)

    print(guess)

    high=x
    low=1
    feedback=''

    while feedback != 'c':
        feedback = input(f"Is {guess} too high (H/h), too low (L,l) or correct (C,c) : ").lower()

        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
        else :
            print(f"Yay! The Computer guessed your number, {guess}, correctly !")

    
    guessUser(12)


