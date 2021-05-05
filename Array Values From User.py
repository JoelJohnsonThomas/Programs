from array import *

arr = array("i", [])

n = int(input("Enter the length of the variable:"))

for i in range(n):
    x = int(input("Enter the Values:"))
    arr.append(x)
print(arr)

s = int(input("Enter the Value to search:"))
j = 0
for e in arr:
    if s == e:
        print("Found at", j)
        break
    j += 1
