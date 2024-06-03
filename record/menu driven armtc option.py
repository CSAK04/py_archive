#menu driven-all arithmetic operationd
n1,n2=eval(input("enter first number:")),eval(input("enter second number:"))
o=input("""+ for addition\n- for subtraction\nx for multiplicaton
/ for division\n^ for exponentiation\nenter operation:""")

if o == "+":
  print("sum is",n1+n2)
  
elif o == "-":
  print("difference is",n1-n2)
elif o == "x":
  print("product is",n1*n2)
elif o == "/":
  try:
    print("quotient is",n1//n2)
    print("remainder is",n1%n2)
  except ZeroDivisionError:
    print("""you cannot divide a number by zero
any number divided by zero is not defined""")
elif o == "^":
  print("",n1**n2)
else:
  print("invalid operator")
