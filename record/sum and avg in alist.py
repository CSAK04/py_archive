#to find sum and average of elements in a list
n=None
while n==None:
  try:
    n=int(input("enter limit:"))
  except ValueError:
    print("limit is a number")
    n=None
s,a,i=0,[],0
print()

while i<n:
  try:
    g=int(input("enter a number:"))
    a.append(g)
    i+=1
  except ValueError:
    print("you are supposed to only enter numbers")
for i in range(len(a)):
  s+=a[i]
avg=s/n
print("\nsum:",s,"\naverage:",avg)
