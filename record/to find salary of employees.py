#TO FIND SALARY OF EMPLOYEES
emp = dict()
n = int(input("Enter number of entries:"))

for i in range(n):
  name = input("Enter name:")
  basic = float(input("Enter basic salary:"))
  hra = float(input("Enter House Rent Allowance:"))
  ca = float(input("Enter Conveyance Allowance:"))

  emp[name] = (basic, hra, ca)

l = emp.keys()
print("\nName\t\t\tNet Salary")
for i in l:
  salary = 0
  z=emp[i]
  for j in z:
    salary+=j
  print(i,"\t\t\t",salary)
