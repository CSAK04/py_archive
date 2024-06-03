def sum(l):
  s = 0
  for i in l:
    s += i
  return s


def pro(l):
  p=1
  for i in l:
    p *= i
  return p


ls = list()
n = int(input("Enter Limit:"))

for i in range(n):
  item = int(input("Enter Number:"))
  ls.append(item)

print("sum:",sum(ls),"pro:",pro(ls))
