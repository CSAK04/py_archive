#import list funct
def inputlist():
    a=list()
    l = int(input("LIMIT:"))
    for i in range(l):
        item = int(input("ENTER ITEM TO ADD TO LIST:"))
        a.append(item)
    return a
