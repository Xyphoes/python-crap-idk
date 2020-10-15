import random
randomint = random.randint(1, 20)
print("Input a random number")
Guess = int(input())
Chances = 0

if Guess > randomint:
    print("Your guess was too high")
else:
    print("The guess is too low")

while Guess != randomint:
    Chances = Chances + 1

Guess = int(input())
if Guess < randomint:
    print("You guessed too low")
if Guess > randomint:
    print("You guessed too high")
if Guess == randomint:
    print("You guessed correct! It took you " + str(Chances) +  " guesses to find the answer.")