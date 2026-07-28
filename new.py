import random
jackpot = random.randint(1,100)
guess = int(input("chal guess kar bete"))
couner = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else :
        print("guess lower")
    guess=int(input("chal guess de"))
    couner+=1
    
    print("sahi ans")
    print("you took",couner,"attempts")