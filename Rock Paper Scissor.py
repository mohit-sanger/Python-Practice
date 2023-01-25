Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random
a = input('Choose any one form rock , paper, scissors')
b = [Rock,Paper,Scissors]
c = random.choice(b)
if a == c:
    print(f' {c} Its Tie')
elif a == 'rock' and c == Paper:
    print(f' {c} You loose')

elif a == 'rock' and c == Scissors:
    print(f' {c} You Won')

elif a == 'paper' and c == Rock:
    print(f' {c} You Won')

elif a == 'paper' and c == Scissors:
    print(f' {c} You loose')

elif a == 'scissors' and c == Paper:
    print(f' {c} You Won')

elif a == 'scissors' and c == Rock:
    print(f' {c} You loose')

else :
    print('Please provide correct input')