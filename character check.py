char=input("enter a character")

if char >= "a" and char<="z":
    print("you have entered a lowercase alphabet")
elif char >= "A" and char<="Z":
    print("you have entered a uppercase alphabet")
elif char >= "0" and char<="9":
    print("you have entered a number")
else:
    print("you have entered a special character")
