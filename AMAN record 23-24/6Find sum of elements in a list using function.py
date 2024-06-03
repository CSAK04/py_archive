#Find sum of elements in a list using function
def sum(l):
  s = 0
  for i in l:
    s += i
  return s

ls = list()
n = int(input("Enter Limit:"))

for i in range(n):
  item = int(input("Enter Number:"))
  ls.append(item)

print("sum of elements:",sum(ls))
