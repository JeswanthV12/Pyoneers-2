"""
from .Homework2 import cal1
print(cal1)

listName = ["apple", "pear", "bannana", "dragonfruit", "lyche"]
print(len(listName))

listName.remove("apple")
listName.remove("lyche")
print(listName)


listName2 = ["apple", "pear", "bannana", "dragonfruit", "lyche"]
print(len(listName2))

listName2.pop(0)
listName2.pop(3)
print(listName2)

listName.extend(listName2)
print(listName)

var = list(("hi","bye","ay"))
print(var)
"""
import random

number = random.randint(1,20)

print("Guess my number from 1 to 20:")
guess = int(input())

if guess == number:
  print("Correct")
elif guess > number and guess <= 20:
  print("Lower")
  guess1 = int(input())
  if guess1 > number:
    print("lower")
  elif guess1 < number:
    print("Higher")
  else:
    print("Correct")
  guess2 = int(input())
  if guess2 > number:
    print("lower")
  elif guess2 < number:
    print("Higher")
  else:
    print("Correct")
elif guess < number and guess <= 20:
  print("Higher")
  guess1 = int(input())
  if guess1 > number:
    print("lower")
  elif guess1 < number:
    print("Higher")
  else:
    print("Correct")
  guess2 = int(input())
  if guess2 > number:
    print("lower")
  elif guess2 < number:
    print("Higher")
  else:
    print("Correct")

if guess > 20 or guess1 > 20:
  print("invalid number")