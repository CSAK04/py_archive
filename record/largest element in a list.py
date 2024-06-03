#to find largest elements in a list
n=int(input("enter limit:"))
a=[]
i=0

while i<n:
  try:
    g=int(input("enter a number:"))
    a.append(g)
    i+=1
  except ValueError:
    print("you are supposed to only enter numbers")
print("largest element is",max(a))          
