#TEXT FILES – DISPLAY  WORDS  WHICH HAS LESS THAN FOUR CHARACTERS
t = open('file.txt','r')

r = t.read()
d = r.split()
c = 0

for i in d:
    if len(i)<4:
        print(i)
t.close()
