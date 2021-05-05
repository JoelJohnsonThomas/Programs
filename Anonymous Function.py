f = lambda a: a * a  # Finding the Square Number
a = int(input("Enter the Number:"))
print("The Square Number of", a, "is", f(a))

x = lambda n, m: n + m  # Addition
n = int(input("Enter a number:"))
m = int(input("Enter another number:"))
print("The addition of", n, "and", m, "is", x(n, m))

y = lambda k, t: k - t  # Subtraction
k = int(input("Enter the number:"))
t = int(input("Enter another number:"))
print("The Subtraction of", k, "and", t, "is", y(k, t))

h = lambda t, r: t * r  # Multiplication
t = int(input("Enter the number:"))
r = int(input("Enter another number:"))
print("The Multiplication of", t, "and", r, "is", h(t, r))


c = lambda o, p: o / p  # Division
o = int(input("Enter the number:"))
p = int(input("Enter another number:"))
print("The Division of", o, "and", p, "is", c(o, p))
