def selectionsort(list):
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
l=[]
m=int(input('Enter The Number Of Elements To Be Added:'))
for k in range(m):
    e=int(input("Enter The Element To Be Added:"))
    l.append(e)
selectionsort(l)
print(l)



