import time


def isEmpty(s):
    if len(s)==0:
        return True
    else:
        return False


def push(s,i):
    s.append(i)
    top = len(s)-1


def pop(s):
    if isEmpty(s):
        return "underflow"
    else:
        val = s.pop()
        if len(s) == 0:
            top = None
        else:
            top = len(s)-1
        return val


def peek(s):
    if isEmpty(s):
        return "Underflow"
    else:
        top = len(s)-1
        return s[top]


def show(s):
    if isEmpty(s):
        print("Empty stack")
    else:
        t = len(s) - 1
        print("(TOP)",end="")
        while t >=0:
            print(s[t],end="<==")
            t -= 1
        print()



s = []
top = None
while True:
    print("**********5T4CK D3M0*************")
    print("1 : PUSH\n2 : POP\n3 : DISPLAY\n4 : PEEK\n0 : EXIT")
    c = int(input("\nENTER YOUR CHOICE:"))
    if c == 0:
        print("shutting down program in 2 seconds")
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("0\nshutting down")
        break
    elif c == 1:
        item = int(input("ITEM TO PUSH:"))
        push(s,item)
        print("ITEM  PUSHed TO stack")
    elif c == 2:
        val = pop(s)
        if val == "underflow":
            print("Empty stack")
        else:
            print("DELETED ITEM:",val)
    elif c == 3:
        show(s)
    elif c == 4:
        val = peek(s)
        if val == "Underflow":
            print("Empty stack")
        else:
            print("TOP ITEM :",val)
    else:
        print("!!!!!!!!!!  ARE YOU IBADH !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print()
