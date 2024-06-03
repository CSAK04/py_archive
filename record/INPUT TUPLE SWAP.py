t=()
t2=()

n=int(input("limit OF FIRST TUPLE:"))
i=0

while i<n:
  a=int(input("enter number:"))
  t+=(a,)
  i+=1

n2=int(input("\nlimit of SECOND TUPLE:"))

for i in range(n2):
  d=int(input("enter number:"))
  t2+=(d,)

print("BEFORE SWAPPING\nfirst tuple:",t,
      "\nsecond tuple:",t2)
t,t2=t2,t
print("\nafter swapping","\nfirst tuple:",
      t,"\nsecond tuple:",t2)
