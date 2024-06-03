#To print nfibonacci series using function

def fibo(n):
    n1,n2,n3,i=0,1,0,0

    print("Fibonacci series")
    while i<n:
            print(n1)
            sum=n1+n2
            n1=n2
            n2=sum
            i += 1

n=int(input("enter required number of terms"))
fibo(n)
