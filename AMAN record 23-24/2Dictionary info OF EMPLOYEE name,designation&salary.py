#Dictionary info OF EMPLOYEE name,designation&salary
emp = dict()
n = int(input("Enter number of entries:"))

for i in range(n):
  name = input("Enter EMPLOYEE name:")
  slr = float(input("Enter EMPLOYEE salary:"))
  Dsn = input("Enter EMPLOYEE Designation:")

  emp[name] = (slr, Dsn)

l = emp.keys()
print("\nName\t\t\tDesignation\t\tSalary")
for i in l:
    print(i,"\t\t\t",emp[i][1],"\t\t\t",emp[i][0])
