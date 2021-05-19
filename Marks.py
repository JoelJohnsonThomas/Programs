from time import sleep


class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = self.m3 + other.m3


print("Send The Details Of Three Students")
sleep(1)
num1 = input("Enter The Name Of The First Student : ")
num2 = input("Enter The Name Of The Second Student : ")
num3 = input("Enter The Name Of The Third Student : ")
sleep(1)
print("Mark List :")

n1 = int(input("Enter the Physics Mark of  " + num1 + " : "))
n2 = int(input("Enter The Chemistry Mark  Of " + num1 + ": "))
n3 = int(input("Enter The Biology  Mark of " + num1 + " : "))

p1 = int(input("Enter The Physics Mark Of " + num2 + ":"))
p2 = int(input("Enter The Chemistry Mark Of  " + num2 + ":"))
p3 = int(input("Enter The Biology Mark Of " + num2 + ":"))

q1 = int(input("Enter The Physics Mark Of " + num3 + ":"))
q2 = int(input("Enter The Chemistry Mark Of " + num3 + ":"))
q3 = int(input("Enter The Biology Mark Of " + num3 + ":"))

s1 = Student(n1, n2, n3)
s2 = Student(p1, p2, p3)
s3 = Student(q1, q2, q3)

mark1 = (s1.m1 + s1.m2 + s1.m3) // 3
mark2 = (s2.m1 + s2.m2 + s2.m3) // 3
mark3 = (s3.m1 + s3.m2 + s3.m3) // 3

if mark1 > mark2 and mark1 > mark3:
    print("1st     Rank   : " + num1 + " : ", mark1, "%")
elif mark1 < mark2 and mark1 > mark3:
    print("2nd     Rank   : " + num1 + " : ", mark1, "%")
elif mark1 < mark2 and mark1 < mark2:
    print("3rd   Rank   : " + num1 + " : ", mark1, "%")

if mark2 > mark1 and mark2 > mark3:
    print("1st     Rank   : " + num2 + " : ", mark2, "%")
elif mark2 < mark1 and mark2 > mark3:
    print("2nd     Rank   : " + num2 + " : ", mark2, "%")
elif mark2 < mark1 and mark2 < mark3:
    print("3rd   Rank   : " + num2 + " : ", mark2, "%")
if mark3 > mark1 and mark3 > mark2:
    print("1st     Rank   : " + num3 + " : ", mark3, "%")
elif mark3 < mark1 and mark3 > mark2:
    print("2nd     Rank   : " + num3 + " : ", mark3, "%")
elif mark3 < mark1 and mark3 < mark2:
    print("3rd   Rank   : " + num3 + " : ", mark3, "%")
