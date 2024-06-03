#To find largest element in a list
def inputlist():
    a=list()
    l = int(input("LIMIT:"))
    for i in range(l):
        item = int(input("ENTER ITEM TO ADD TO LIST:"))
        a.append(item)
    return a

def maxOfList(l):
    max = l[0]
    for i in range(len(l)):
        if l[i]>max:
            max = l[i]
    print("largest element in list is :",max)
maxOfList(inputlist())
