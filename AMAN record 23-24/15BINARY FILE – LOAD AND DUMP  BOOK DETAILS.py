#BINARY FILE – LOAD AND DUMP  BOOK DETAILS
from pickle import *
f = open("file.dat","wb")
n = int(input("limit:"))

for i in range(n):
    print("BOOK No.:",i+1)
    t = input("BOOK TITLE:")
    p = input("BOOK PRICE:")
    r = t + ' $' + p + '\n'
    dump(r,f)
    
f.close()
t = open("file.dat","rb")
for i in range(n):
    print(load(t))
t.close()
