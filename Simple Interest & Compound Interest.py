P = float(input("Enter The Value Of The Principal : "))

R = float(input("Enter The Value Of Rate : "))

n = int(input("Enter The Value Of Time : "))

SI = (P * n * R) / 100

Q = 1 + (R / 100)

CI = P * pow(Q, n) - P

print("Simple Interest : ",SI)
print("Compound Interest : ",CI)
