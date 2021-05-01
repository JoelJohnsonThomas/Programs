# fetching the prime number from the list given by the user
n = int(input("enter the number of elements you want:"))  # to get the  number of elements from the user
l = []  # introducing a variable in order to get the list
for i in range(n):
    b = int(input("enter the number:"))  # getting  numbers from the user
    l.append(b)  # including the given numbers in the list
l.sort()  # arranging the numbers in ascending order
print("The given list:", l)
for j in l:
    if j % 2 == 0:  # to fetch the prime numbers 
        print("Prime number:", j)
    else:   # to fetch  the composite numbers
        print("composite number:", j)
