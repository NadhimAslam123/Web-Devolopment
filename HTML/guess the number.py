import random

def guess_the_number():
    number_to_guess = random.randint (1,100)
    atempts = 0

    print("Welcome to Guess the Number")
    print("I am thinking of a number between 1 and 100")

    while True:
        try:
            guess = int(input("Take a guess:"))
            atempts += 1
            if guess < number_to_guess:
             print("Too Low")
            elif guess > number_to_guess:
               print("Too High")
            else :
               print(f"Cogratulations! you guess the number in {atempts} tries")
               break
        except ValueError:
           print("Please enter a valid ineger")
guess_the_number()