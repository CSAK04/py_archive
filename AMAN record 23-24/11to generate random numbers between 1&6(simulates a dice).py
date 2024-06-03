#to generate random numbers between 1&6(simulates a dice)
import random
def dice():
  r=random.randint(1,6)
  print("your dice rolled",r)

print("enter 'dice' to roll the dice")
while True:
  a = input()
  if a == "dice":
    dice()

