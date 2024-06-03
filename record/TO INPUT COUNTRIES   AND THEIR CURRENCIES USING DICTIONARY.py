#PROGRAM TO INPUT COUNTRIES   AND THEIR CURRENCIES USING DICTIONARY
count = dict()
n = int(input("Enter Number of Countries:"))

for i in range(n):
  co = input("Enter Country Name:")
  ca = input("Enter Country Capital Name:")
  cu = input("Enter Country Currency Name:")
  count[co] = (ca,cu)

l = count.keys()

print("\nCountry\t\tCapital\t\tCurrency")
for i in l:
  z = count[i]
  print("\n",i,"\t",end="\t")
  for j in z:
    print(j,"\t",end="")
x = input("\nEnter Country to Search:")

for i in l:
  if i == x:
    print("\nCountry\t\tCapital\t\tCurrency")
    z = count[i]
    print(i,"\t\t",end="")
    for j in z:
      print(j,"\t",end="")
    break
