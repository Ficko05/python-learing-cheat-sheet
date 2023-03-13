import random

guess = 0
random_numb = random.randrange(1,10)
print(random_numb)
while guess < 3:
    input_guess = int(input("guess: "))
    if input_guess == random_numb:
        print("you guessed it!!")
        break
    elif input_guess < random_numb:
        print("higher")
        guess += 1
    elif input_guess > random_numb:
        print("lower")
        guess += 1
else:
    print("you failed")

