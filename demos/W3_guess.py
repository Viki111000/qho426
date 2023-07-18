import random #Taking definitions from a package "random" into my scope
x = random.randint(0,20)
print("Welcome to my Guess Game! Iam thinking of a number between 1 and 20")
for attempts in range(1,6):
    print(f"Attempt nr{attempts}")
    guess = int(input("Take a guess"))
    if guess == secret_n:
        print("Congrats!You have guessed correctly!")
        break
    elif secret_n < guess:
        print("Too high!")
    else:
        print("Too low!")
if guess   == secret_n:
        print(f"Game over! My number was {secret_n}")



