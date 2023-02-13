#RPS Game  
import random


user_name =input ("What is your name? ")
user = user_name
print(f"Welcome {user}!")
user_ans = ''

user_ans = input("Are you ready to play ROCK, PAPER, SCISSORS? (yes or no?) ")

if user_ans.lower() == 'yes':
    print("Alright, Let's play! \n")
    #continue
    def get_choices():  #get_choices is a function  
      player_choice = input("Enter a choice (rock, paper, scissors): ")
      options = ['rock', 'paper', 'scissors']
      computer_choice = random.choice(options)
      choices = {"player":player_choice, "computer":computer_choice}
      return choices 
    
    def check_win(player, computer ):
      print(f"You chose {player}, computer chose {computer}.")
    
      if player == computer:
        return "It's a tie!"
        #if player chooses "ROCK"
      elif player == "rock":
        if computer == "scissors":
          return "Rock smashes scissors! You win!"
        else:
          return "Paper covers rock! You lose :("
    
      #if player chooses "PAPER"
      elif player == "paper":
        if computer == "rock":
          return "Paper covers rock! You win!"
        else:
          return "Scissors shred paper! You are a loser :("
    
      #if player chooses "SCISSORS" 
      elif player == "scissors":
        if computer == "paper":
          return "Scissors shread paper! You win!"
        else:
          return "Rock crushes scissors! You lost :("
    
    
    choices = get_choices()
    result = check_win(choices["player"], choices['computer'])
    print(result)
    
elif user_ans.lower() == 'no':
    print('Not ready to play? Okay, see ya later!')
    exit()
else:
    print('Type yes or no')
    