str=input("enter:")
d,l,c,s=0,0,0,0
for i in str:
  if (i.isdigit()):
    d+=1
  if(i.isalpha()):
    l+=1
  if(i.isspace()):
    s+=1
  c+=1
print("no. of digits:",d,"\nno. of alphabets:",l,"\nno. of characters:",c,"\nno. of space:",s)
