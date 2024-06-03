#string palindrome
n=input("enter string:")

n=n.casefold()

if n == n[::-1]:
  print("THIS IS A PALINDROME")
else:
  print("THIS IS NOT A PALINDROME")
