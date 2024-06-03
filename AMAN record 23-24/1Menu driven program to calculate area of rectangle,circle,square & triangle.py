#Menu driven program to calculate area of rectangle,circle,square & triangle
from math import *
o = "Y"


while o in "Yy":
    print("\nEnter corresponding data to calculate Area of",
          "\n1.Rectangle\n2.Square\n3.Circle\n4.Triangle")
    
    opt = input("\nYour choice:")

    while opt not in "1234":
        opt = input("Enter a valid data to continue:")
    if opt == "1":
        l = float(input("\nEnter Length of Rectangle:"))
        b = float(input("Enter Breadth of Rectangle:"))
        print("Area of Rectangle =",l*b)
    elif opt == "2":
        l = float(input("\nEnter Side Length of Square:"))
        print("Area of Square:",l**2)
    elif opt == "3":
        l = float(input("\nEnter Radius of Circle:"))
        print("Area of Circle:",pi*l**2)
    elif opt == "4":
        l = float(input("\nEnter Height of Triangle:"))
        b = float(input("Enter Base of Triangle:"))
        print("Area of Triangle:",l*b/2)
        
    o = input("\nDo you wish to Continue(Y/y to continue):")
