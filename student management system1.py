
name = input("Enter Your Name:")

student = {"English":0,"Maths":0}
l = student.keys()
print(l)
print("Enter Your Marks")
for i in range(len(l)):
  mark = int(input(str(l[i])+":"))
  student[l[i]]=mark
print(student["English"])
print(student["Maths"])
