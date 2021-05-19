n = int(input("Enter The Upper Limit :"))
print("The Odd Numbers are :")
for num in range(2, n + 1):
    if num % 2 == 0:
        continue
    else:
        print(num)
