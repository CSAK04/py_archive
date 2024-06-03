#number palindrome check
n=int(eval(input("enter number:")))

t=n
rev=0

while t != 0:
  rev=(rev*10)+(t%10)
  t=int(t/10)

if n == rev:
  print("number is palindrome")
else:
  print("number is not palindrome")
