variable="strinGs  @s 12345s +_s  pYtHoNs"
print (variable)


#to print no. of characters in a string
print(len(variable))


#makes first letter capital
print(variable.capitalize())

'or'

x=variable.split()
variable2=""
for i in x:
    variable2 += i.capitalize()+" "
print(variable2)


#breaks string at specified seperators or spaces and returns a list of substrings
print(variable.split())
print(variable.split("s"))

#replaces the old string by new string
print(variable.replace("pYtHoN","c++"))

#find
print(variable.find("1234"))
