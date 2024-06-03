#To find largest of 2 numbers using function

def lORs(num1,num2):
    if(num1>num2):
        print(num1,"is greater than",num2)
    elif(num1<num2):
        print(num1,"is less than",num2)
    else:
        print(num1,"is equal to",num2)


n1= eval(input("enter a number"))
n2=eval(input("enter another number"))
lORs(n1,n2)
