#TEXT FILES – NUMBER OF LINES STARTING WITH  ‘A’

t = open('file.txt','r')

r = t.readlines()
c = 0

for i in range(len(r)):
    if r[i][0] in "Aa":
        c += 1
print("number of lines starting with a :",c)
t.close()
