#function to double element in list
def inlist():
    l = list()
    n = int(input("Enter Limit:"))
    for i in range(n):
        item = eval(input("Enter Number to add to List:"))
        l.append(item)
    return l


def doubleList(s):
    for i in range(len(s)):
        s[i]=s[i]*2
    print(s)
doubleList(inlist())
