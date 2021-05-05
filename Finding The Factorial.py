def fact(n):  # finding the factorial using the FOR loop
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


n = int(input("Enter the Factorial number you want:"))

print("The Factorial number of", n, "is", fact(n))
