#fibonnaci
n=int(input("enter no. of terms:"))
n1=0
n2=1
print("fibonacci series of",n,"numbers")
i=0
while i<n:
  print(n1,end=" ")
  s=n1+n2
  n1=n2
  n2=s
  i+=1
