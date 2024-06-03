#input,split&sort list into words
def words(s):
  a = s.split()
  a.sort()
  print(a)

srt = input("enter the sentence:")
words(srt)
