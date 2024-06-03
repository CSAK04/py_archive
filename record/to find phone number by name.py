 #to find phone number by name
phone = dict()

n = int(input("Enter number of entries:"))

for i in range(1,n+1):
  name = input("Enter name:")
  phone_no = int(input("Enter phone number:"))
  phone[name] = phone_no

li = phone.keys()

x = input("Enter Name to search for Phone_number:")

for i in li:
  if i == x:
    print(phone[i])
    break
else:
  print(x," not found")
