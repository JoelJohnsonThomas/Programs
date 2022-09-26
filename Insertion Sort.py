def insertionsort(list):
    for i in range(1,len(list)):
        temp =list[i]
        j =i-1
        while( j>=0 and temp < list[j]):
            list[j+1]=list[j]
            j =j-1
            list[j+1]=temp
l=[]
m=int(input('Enter The Number Of Elements To Be Added:'))
for k in range(m):
    e=int(input("Enter The Element To Be Added:"))
    l.append(e)
insertionsort(l)
print(l)



