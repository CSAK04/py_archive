#linear search
n=int(input("limit:"))
l=[]

for i in range(n):
  item=eval(input("enter number:"))
  l.append(item)

p=eval(input("enter no to search:"))

pos=-(len(l)+1)
poss = pos

for i in range(n):
  if l[i]==p:
    pos=i

if pos==poss:
  print("item not found")
else:
  print("\nITEM FOUND AT\nindex:",pos,"\nand position",pos+1)
