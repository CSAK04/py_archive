from input_list import inputlist
#add alternayte
def addAlter(a):
    s = 0
    for i in range(len(a)):
        if i % 2 == 0:
            s += a[i]

    return s

l = inputlist()
print("sum of alternate elements is:",addAlter(l))
