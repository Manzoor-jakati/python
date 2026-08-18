import random

secret_number = random.randint(1,50)

attempts = 0

while True:
    try:

        user = int(input("Guess the Number : "))
        attempts += 1
        if user == secret_number:
            print(f"You guessed it Right : {secret_number}")
            break
        elif user > secret_number:
            print(f"Nah, That is too high , RETRY")
        elif user < secret_number:
            print(f"Nah, Thats too low , RETRY")
        else:
            break
    except ValueError:
        print("this is not a valid number")

print(f"You guessed it right {secret_number} , your total attempt is {attempts} ")

