#sum and product in a list
n=int(input("enter limit"))
list=[]
s=0
p=1

for i in range(0,n):
    item=int(input("enter value"))
    list.append(item)
    s=s+item
    p=p*item
print(list,s,p,sep='\n')
