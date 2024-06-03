#factorial of a number using function

def fact(num):
    num=num+1
    fac=1
    for i in range(1,num):
        fac=fac*i
        print(fac)

i = int(input("Enter number to find factorial:"))
fact(i)
    
