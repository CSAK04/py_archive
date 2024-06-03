#simple interest

def si(p,r,t = 10):
      si = p*r*t/100
      amount = p+si
      print(amount)
      return amount


def comma(a):
      a *= 100
      f = str(int(a))
      j = ""
      s =-1
      for i in f[::-1]:
        if s == 0:
          j += i+"."
        elif s % 3 == 0:
          j += i+","
        else:
          j += i
        s += 1
        p = j[::-1]
      if p[0] == ",":
        p = ""
        s = 0
        for i in j:
          if s == len(j)-1:
            p += i
            s += 1
      else:
        p=j
      return p[::-1]

while True:
  p = float(input("Enter Principle:"))
  r = float(input("Enter rate of interest:"))
  t = float(input("Enter number of years:"))

  print("you have to pay Rs."+comma(si(p,r,t)))

  a = input("Do You Want To Quit(Y/N):")
  a = a.upper()
  
  if a == "Y":
    break
