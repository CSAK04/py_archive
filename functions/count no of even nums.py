#count number of even numbers
from input_list import *

def numEvenNum(a):
    s = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            s += 1
    return s
print("No. of Even Numbers in the list is ",numEvenNum(inputlist()))
