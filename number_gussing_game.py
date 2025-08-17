# 3. Python program to implement a simple Number Guessing Game.

import random

def number_guessing_game():
  """
  This function runs a number guessing game.
  The computer picks a number between 1 and 100, and the user tries to guess it.
  """
  # Generate a random secret number between 1 and 100 (inclusive)
  secret_number = random.randint(1, 100)
  attempts = 0
  guess = 0 # Initialize guess to a value that won't match the secret number

  print("--- Number Guessing Game ---")
  print("I have selected a secret number between 1 and 100.")
  print("Can you guess what it is?")
  print("----------------------------")

  # Loop until the player guesses the correct number
  while guess != secret_number:
    try:
      # Prompt the player for their guess
      guess_input = input("Enter your guess: ")
      guess = int(guess_input)
      attempts += 1 # Increment the attempt counter

      # Provide feedback to the player
      if guess < secret_number:
        print("Too low! Try again.")
      elif guess > secret_number:
        print("Too high! Try again.")
      else:
        # The guess is correct
        print("\n=================================================")
        print(f"🎉 Congratulations! You've guessed the number!")
        print(f"The secret number was {secret_number}.")
        print(f"It took you {attempts} attempts to guess correctly.")
        print("=================================================")

    except ValueError:
      # Handle cases where the input is not a valid number
      print("Invalid input. Please enter a whole number.")

# --- Main part of the program ---
if __name__ == "__main__":
  # Start the game
  number_guessing_game()
