def swaplist(newlist):
    size =len(newlist)-1
    temp =newlist[0]
    newlist[0]=newlist[size]
    newlist[size]= temp
    return newlist
n= int(input("How many numbers you want to enter in the list?:"))
list=[]
for i in range(n):
    nums = int(input("Enter The Number In the List:"))
    list.append(nums)
print("Before Swapping:",list)

print("After Swapping:",swaplist(list))
