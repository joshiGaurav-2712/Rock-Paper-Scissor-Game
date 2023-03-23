import random  
user_wins=0
computer_wins=0

options=["rock","paper","scissor"]
#           0       1       2
print("Welcome to rock/paper/scissor game!")

while (user_choice:=input ("Enter user's choice(rock/paper/scissor/quit):").lower()) != "quit":
  if user_choice not in options:
      continue
  random_no=random.randint(0,2)
  computer_choice=options[random_no]
  print(f"Computer's choice is {computer_choice}.")
  if  user_choice=="rock" and computer_choice=="scissor":
      print("Congratulations user you won!")
      user_wins+=1
  elif user_choice=="paper" and computer_choice=="rock":
      print("Congratulations user you have won!")
      user_wins+=1 
  elif user_choice=="scissor" and computer_choice=="paper":
      print("Congratulations user you have won!")
      user_wins+=1 
  else:
      print("Computer has won!")
      computer_wins+=1 


print(f"User wins {user_wins} time.")
print(f"Computer wins {computer_wins} time.")
print("Thank you for playing!")
