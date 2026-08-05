import random

play_again = "y"

while play_again == "y":
  print("welcome player\nI'm thinking of a number between 1 and 100")
  print("you have 6 attempts to guess it\n")

  attempt = 0
  secret_num = random.randint(1, 100)
  won = False

  while attempt < 6:
    attempt += 1
    print(f"attempt {attempt}/6")
    guess = int(input("Enter your guess: "))

    if guess == secret_num:
      print("\ncongratulations!\nyou guessed the number")
      won = True
      rounds_won+=1
      break
    elif guess - secret_num > 10:
      print("too high")
    elif guess - secret_num > 0:
      print("higher")
    elif secret_num - guess > 10:
      print("too low")
    else:
      print("lower")

  if not won:
    print(f"\nGame over! the secret number was {secret_num}")

  play_again = input("Play another round? (y/n): ")