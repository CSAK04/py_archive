#to calculate median and average of data
from statistics import *

n = int(input("Enter number of students:"))
l=list()

for i in range(n):
  height = float(input("enter height of student:"))
  l.append(height)

avg = mean(l)
med = median(l)

print("Average height is ",int(avg),"\nMedian height is ",int(med))
