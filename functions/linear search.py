def search(w):
  found = False
  num = int(input("Enter number to Search:"))
  
  for i in range(len(w)):
    if w[i] == num:
      pos = i
      found = True
      break
    
  if found ==True:
    print("Item found at Index ",pos," position ",pos+1)
  else:
    print("Not Found")

l = list()
n = int(input("Enter LIMIT:"))

for i in range(n):
  item = int(input("enter a item:"))
  l.append(item)
search(l)
