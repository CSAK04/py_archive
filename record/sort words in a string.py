#SORTING WORDS IN A STRING
a=input("ENTER ANYTHING:")
b=a.split()
for j in range(len(b)-1):
  for i in range(len(b)-1):
    if b[i]>b[i+1]:
      b[i],b[i+1]=b[i+1],b[i]
print("LIST AFTER SORTING:",b)
