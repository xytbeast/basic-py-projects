import random 

def guess(x):
    randomno = random.randint(1,x)
    guess=0
    while guess !=randomno:
        guess = int(input(f"guess no btw 1 to {x}:"))
        if guess < randomno:
            print("sry too low try again")
        elif guess > randomno:
            print("sry too high try again")    
    print("congrats right no")        

guess(10)    