import random

def guessFunction(x):
    random_num = random.randint(1,x)
    guess=0

    while (guessFunction != random_num) :
        guess=int(input(f"Enter any number between 1 and {x} : "))

        if random_num < guess:
            print("Go Lowerrr !")
        
        elif random_num > guess:
            print("Go Higherrr !")

        else :
            print(f"Yayy Congrats! You guess random number {random_num} correctly! Bravo." )

     
                  


guessFunction(10)
