import random

guess_number = int(input("Enter a number between 1-5"))
random_number = random.randint(1, 5)
if guess_number == random_number:
    print("You Have Win")
else:
    print("you Have lost")
    print(f"random number was {random_number}")