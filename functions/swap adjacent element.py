#swap adjacent nums
from input_list import *

def swapadj(l):
    for i in range(0,len(l)-1,2):
        l[i],l[i+1] = l[i+1],l[i]
    print(l)
swapadj(inputlist())
