import random

while True:

  choices = ['rock','paper','scissors']

  computer = random.choice(choices)
  player = None


  while player not in choices:
     player = input('rock,paper or scissors ').lower()

     if player == computer:
      print("computer: ",computer)
      print('player: ',player)
      print('tie')
     elif player =='rock':
      if computer == 'paper':
         print("computer: ",computer)
         print('player: ',player)
         print('You loose')
     if computer == 'scissors':
                print("computer: ",computer)
                print('player: ',player)
                print('You win')
     elif player =='scissors': 
      if computer == 'rock':
         print("computer: ",computer)
         print('player: ',player)
         print('You loose')
      if computer == 'paper':
                print("computer: ",computer)
                print('player: ',player)
                print('You win') 
     elif player =='paper': 
      if computer == 'scissors':
         print("computer: ",computer)
         print('player: ',player)
         print('You loose')
      if computer == 'rock':
                print("computer: ",computer)
                print('player: ',player)
                print('You win')

     play = input("play  again (yes/No): ").lower()
  
     if play !='yes':
      break
  print('bye')