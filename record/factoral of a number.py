#factorial of a number
n=int(input("enter a number:"))
p=1

for i in range(1,n+1):
  p*=i
print(n,"factorial is",p)
