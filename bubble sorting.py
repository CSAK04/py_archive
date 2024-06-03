#bubble sorting
a=int(input ("enter limit:"))
list=[]
for num in range(a):
    item=int(input("enter number:"))
    list.append(item)

for i in range(a-1):
    for j in range(a-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("after sorting:",list)
