#string built-in
str="jkcv@  djbf435876@nbdvb    hiUFd@457986bjhcv    khgfdj@87645bhjhv"
#len
print(len(str))

#capitalize
print(str.capitalize())

#capitalize2
str1=""
x=str.split()
for i in x:
    str1+= i.capitalize()+" "
print(str1)

#split
print(str.split())

#split2
print(str.split("@"))

#split3
print(str.split("@",2))

#replace
strr=str.replace("@","#")
print(strr)

#find
print(str.find("43"))

#index
print(str.index("43"))

#is
a="jhfdg"
b="34665"
c="   "
d="ameiraaaaaaaaaaaa"

print(a.isalpha())
print(b.isdigit())
print(c.isspace())
print(d.isalnum())
print(d.islower())
print(d.isupper())
print(d.istitle())


print(d.lower())
print(d.upper())
print(d.title())
print(d.count("a"))
print(a.join("#"))
print(a.join(" 123444444657686789457636757468747876548785678756987498789679845798674857987986578798579845679654"))
print(a.strip())
u="   mnb  b b  v       "
print(u.strip())
print(u.rstrip())
print(u.lstrip())

print(str.swapcase())
print(str.partition("b"))
