def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("Enter the Factorial number you want:"))
print("The Factorial number of", n, "is", fact(5))
