#linear search
n=int(input("limit:"))
l=[]

for i in range(n):
  item=eval(input("enter number:"))
  l.append(item)

p=eval(input("enter no to search:"))

pos=-25

for i in range(n):
  if l[i]==p:
    pos=i

if pos==-25:
  print("item not found")
else:
  print("\nITEM FOUND AT\nindex:",pos,"\nand position",pos+1)
