b=input("enter anything:")
a,c=0,0
x=b.split()

for i in x:
  a+=1
for i in b:
  if i in "aeiouAEIOU":
    c+=1
print("Words:",a,"\nVowells:",c)
