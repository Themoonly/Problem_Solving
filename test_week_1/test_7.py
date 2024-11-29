# เกมทายตัวเลข
import random 

print("welcome to the number guessing game!")
print("i'm thinking of a number between 1 and 100. can you guess is it?")

x = random.randint(1,100)
print(x)

attempts = 1
while True:
    number = int(input("Enter you guess: "))

    if number == x:
        print(f"congratulation! You guessed the number is {attempts} attempts.")
        break
    else:
        if number > x:
            print("Too high! try again" )
        else:
            print("Too low! try again" )
        attempts += 1


