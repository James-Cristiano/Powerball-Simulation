"""Powerball Lottery.
A simulation of the Powerball lottery. So you can try and win
without having to waste your hard-earned money!!
"""

print('''This is a simualtion of the Powerball Lottery. 
      
      The cheapest ticket in AUS is $8.10 and the odds of you hitting
      the jackopt is - 1 in 76,767,600!! Since the odds are not exactly in our favour, 
      here is a little taste of being able to play without the need of spending all of your money.''')

#Player picking their numbers: 1 - 35
import random
while True:
      print('Enter 7 different numbers between 1 and 35, include spaces inbetween each one.')
      print('e.g: 1 19 24 12 8 9 21')
      Response = input('> ')
      
      #making sure the user has choosen 7 numbers
      Numbers = Response.split()
      if len(Numbers) != 7:
            print('Please enter 7 numbers, make sure they are seperated by spaces.')
            continue
      
      #converting the string of numbers into INT's
      try:
            for i in range(7):
                  Numbers[i] = int(Numbers[i])
      except ValueError:
            print('Please enter numbers like the following: 27, 19 or 24')
            continue
      
      #making sure the numbners are inbetween the base range
      for i in range(7):
            if not (1 <= Numbers[i] <= 35):
                  print('All numbers must be between 1 and 35!')
                  continue
      
      #checking if numbers are unique
      if len(set(Numbers)) != 7:
            print('yeah must enter 7 different numbers.')
            continue
      
      break

#choosing the Powerball number: 1 - 20
while True:
      print('Enter the Powerball number between 1 and 20.')
      Response = input('> ')
      
      #converting answer into INT
      try: 
            Powerball = int(Response)
      except ValueError:
            print('Please enter a number like 5, 10, 18')
            continue
      
      #checking if number is between 1 and 20
      if not (1 <= Powerball <= 20):
            print('Powerball number must be between 1 and 20.')
            continue
      break

#entering number of times you want to play
while True: 
      print('How many times do you want to play? (max: 1,000,000 times)')
      Response = input('> ')
      
      #converting answer to INT
      try: 
            NumPlays = int(Response)
      except ValueError:
            print('Please enter a number like 10, 9001, 150000')
            continue
      
      #checking if number matches ranges for games played
      if not (1 <= NumPlays <= 1000000): 
            print('you must choose a number between 1 and 1000000.')
            continue
      break

#running the simulation now
Price = '$' + str(8.10*NumPlays)
print('It costs',  Price, 'to play', NumPlays, 'times, but don\'t')
print('worry. I\'m sure that you\'ll win it all back here.') 
print('Press Enter to start playing...')

PossibleNumbers = list(range(1, 36))
for i in range(NumPlays):
      random.shuffle(PossibleNumbers)
      WinningNumbers = PossibleNumbers[0:7]
      WinningPowerball = random.randint(1, 20)
      
      #Displaying the winning numbers
      print('The winning numbers are: ', end='')
      AllWinningNumbers = ''
      for i in range(7):
            AllWinningNumbers += str(WinningNumbers[i]) + ' '
      AllWinningNumbers += 'and ' + str(WinningPowerball)
      print(AllWinningNumbers.ljust(21), end='')
      
      if (set(Numbers) == set(WinningNumbers) and Powerball == WinningPowerball):
            print()
            print('You have won the Powerball!! Congrats!')
            print('You would be rich if this was real hahaha!')
            break
      else:
            print(' You lost!')
            
print('You have wasted', Price)
print('Thanks for playing!')