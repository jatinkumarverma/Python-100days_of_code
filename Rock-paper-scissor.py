rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
           ______)
       __________)
      (____)
---.__(___)
'''

moves= [rock,paper,scissors]
userMove = input("What do you choose?\n0 for Rock, 1 for Paper & 2 for Scissors.\n")
import random
compMove = random.choice(moves)

if userMove == "0":
  print(f"{rock}\nComputer chose:")
  if compMove == rock:
     print(f"{rock}\nTied!")
  elif compMove == paper:
     print(f"{paper}\nYou Lost!")
  else:
     print(f"{scissors}\nYou Won!")
elif userMove == "1":
  print(f"{paper}\nComputer chose:")
  if compMove == rock:
     print(f"{rock}\nYou Won!")
  elif compMove == paper:
     print(f"{paper}\nTied!")
  else:
     print(f"{scissors}\nYou Lost!")
elif userMove == "2":
  print(f"{scissors}\nComputer chose:")
  if compMove == rock:
     print(f"{rock}\nYou Lost!")
  elif compMove == paper:
     print(f"{paper}\nYou Won!")
  else:
     print(f"{scissors}\nTied!")
else:
  print("Your move isn't available. Please choose between 0 to 2 inclusive")
