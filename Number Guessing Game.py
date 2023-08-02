import random

guesses =[]

myComputer = random.randint(1,70)

player = int(input("Enter a number between 1-70: "))
guesses.append(player)

while player != myComputer:
    if player > myComputer:
        print("Number is too high!")
    else:
        print("Number is too low!")
    player = int(input("Enter a number between 1-70: "))
    guesses.append(player)


else:
    print("You have guessed right! Good job!")
    print("It took you %i guesses. " % len(guesses))
    print("These were your guesses:")
    print(guesses)
