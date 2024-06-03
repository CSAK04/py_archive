#adding element with ending digit 7
from input_list import *

def addendwith7(a):
    sum = 0
    for i in range(len(a)):
        if a[i] % 10 == 7:
            sum += a[i]
    return sum
print("sum of alternate elements is:",addendwith7(inputlist()))
