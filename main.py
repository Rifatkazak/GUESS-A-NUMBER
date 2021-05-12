#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from logo import logo

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 

print(logo)

def game():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  global random_number
  random_number = random.randint(1,100)
  if level=='hard' :
      return guess_hard()
  elif level=='easy':
      return  guess_easy()
   
def guess_hard() :
    print("You have 5 attemps remaining to guess the number. ")
    county  = 5
    while county != 0 :
      county -= 1
      user_number = int(input("Please Guess a Number : "))
      if user_number > random_number :
        print("Too high.")
        print("Guess Again.")
        print(f"You have {county} attempts remaining to guess number.")
        if county == 0:
          print("You've run out of guesses, you lost")
          again = input("Do you want play game again? 'yes' or 'no'")
          if again == 'yes' :
              return game()
          else:
              print("Byeeee")
              break
      elif user_number < random_number:
        print("Too low.")
        print("Guess Again.")
        print(f"You have {county} attempts remaining to guess number.")
        if county == 0:
          print("You've run out of guesses, you lost")
          again = input("Do you want play game again? 'yes' or 'no'")
          if again == 'yes' :
              return game()
          else:
              break
      elif user_number == random_number :
        print(f"Correct ! Number is {random_number}")
        again = input("Do you want play game again? 'yes' or 'no'")
        if again == 'yes' :
          return game()
        else:
          break
        
      
def guess_easy() :
    print("You have 10 attemps remaining to guess the number. ")
    county = 10
    global random_number
    while county!=0 :
      user_number = int(input("Please Guess a Number : "))
      county -= 1
      if user_number > random_number :
        print("Too high.")
        print("Guess Again.")
        print(f"You have {county} attempts remaining to guess number.")
        if county == 0:
            print("You've run out of guesses, you lost")
            again = input("Do you want play game again? 'yes' or 'no'")
            if again == 'yes' :
                return game()
            else:
                break
      elif user_number < random_number:
        print("Too low.")
        print("Guess Again.")
        print(f"You have {county} attempts remaining to guess number.")
        if county == 0:
            print("You've run out of guesses, you lost")
            again = input("Do you want play game again? 'yes' or 'no'")
            if again == 'yes' :
                return game()
            else:
                break
      elif user_number == random_number :
        print(f"Correct ! Number is {random_number}")
        again = input("Do you want play game again? 'yes' or 'no'")
        if again == 'yes' :
          return game()
        else:
          break
      elif user_number != random_number and county==0 :
        print("You've run out of guesses, you lost")
game()
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

