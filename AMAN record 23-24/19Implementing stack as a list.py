#Implement stack as a list
import time
s = []

while True:
    print("1 : PUSH\n2 : POP\n3 : DISPLAY\n4 : PEEK\n0 : EXIT")
    ch = int(input("ENTER YOUR CHOICE:"))
    if ch == 0:
        print("Closing program in 2 seconds")
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("0\nProgram Closed")
        break
    elif ch == 1:
        item = int(input("ITEM TO PUSH:"))
        s.append(item)
        print(item,"pushed to stack")
    elif ch == 2:
        if s == []:
            print("EMPTY STACK")
        else:
            print("DELETED ITEM:",s.pop())
    elif ch == 3:
        if s == []:
            print("EMPTY STACK")
        else:
            l = len(s)
            print("(TOP)",s[-1], end="")
            for i in range(l-2,-1,-1):
                print("<===",end=str(s[i]))
            print()
    elif ch == 4:
        if s == []:
            print("EMPTY STACK")
        else:
            print("TOP ITEM:",s[-1])
    else:
        print("!!!!!!!! INVALID SELECTION !!!!!!!!")
    print()
