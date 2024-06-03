def sum(tu):
  s = 0
  for i in tu:
    s += i
  print(s)


def pro(tu):
  p = 1
  for i in tu:
    p *= i
  print(p)


opt = "y"
t = ()
n = int(input("Limit:"))

for i in range(n):
  a = int(input("Enter Number:"))
  t += (a,)

while opt == "y" or "Y":
  print("enter a choice to do following operations:",
        "\n1 : sum of tuple\n2 : product of tuple",
        "\n3 : max of tuple\n4 : min of tuple")
  
  o = int(input("Enter Your Choice:"))
  
  if o == 1:
    sum(t)
  elif o == 2:
    pro(t)
  elif o == 3:
    print(max(t))
  elif o == 4:
    print(min(t))
  else:
    print("INvld adopretor")

  opt = input("Do you want to Continue(Y or y / N or n):")
