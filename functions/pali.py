def pali(word):
  w = word.upper()
  if w == w[::-1]:
    print("palindrome aaanu!!!!!!!!!")
  else:
    print("not palindrome")

inp = input("Enter a word to check if palindrome:")
pali(inp)
