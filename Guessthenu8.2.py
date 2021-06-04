secret = 99

guess = int(input("Guess the secret number from 1 to 100: "))

if guess == secret:
    print("Congratulations you won!")
else:
    print("Good luck next time!")