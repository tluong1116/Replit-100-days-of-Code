import random

print("Guess the number game!\n")
print("Totally Random One-Million-to-One\n")
number = random.randint(1,1000000)
counter = 1
while True:
    guess = int(input("Enter a number: "))
    if guess == number:
        print("You guessed it!🥳")
        break
    elif guess < number:
        print("Too low!")
        counter += 1
    else:
        print("Too high!")
        counter += 1
print("You guessed it in", counter, "tries!")
