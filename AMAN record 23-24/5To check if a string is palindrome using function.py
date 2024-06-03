#To check if a string is palindrome using function
def pali(word):
  w = word.upper()
  if w == w[::-1]:
    print(word,"is a palindrome")
  else:
    print(word,"is not palindrome")

inp = input("Enter a word to check if palindrome:")
pali(inp)
