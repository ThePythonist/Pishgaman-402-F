from random import choice

number = choice(range(1, 11))
chances = 5

print("Welcome to number guessing game")

while chances > 0:
    print(f"You have {chances} chances")
    guess = int(input("Guess the number : "))
    if guess == number:
        print("You won!")
        break
    elif guess > number:
        print("Try smaller than", guess)
    else:
        print("Try bigger than", guess)
    chances -= 1
else:
    print("Game over! The number was", number)
