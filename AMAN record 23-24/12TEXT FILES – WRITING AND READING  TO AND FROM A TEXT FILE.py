#TEXT FILES – WRITING AND READING  TO AND FROM A TEXT FILE

t = open("file.txt","w")
n = int(input("limit:"))

for i in range(n):
    line = input("Enter  line to insert in file:")
    t.write(line + "\n")

t.close()

t = open("file.txt","r")
for i in range(n):
    print(t.readline())
t.close()
