import random
print("welcome to the number guessing game")
print("i am thinking of a number between 1 and 100")
number=random.randint(1,100)
if input("choose a difficulty type 'easy' or 'hard' ").lower()=="hard":
    live=5
else:
    live=10
game_on=True
while game_on:
    print(f"you have {live} lives")
    guess=int(input("make a guess  "))
    if guess==number:
        print(f"you won the game the, the number:{number}={guess}")
    elif guess>number:
        print("your guess is too high")
        live-=1
    elif guess<number:
        print("you guess is too low")
        live-=1

