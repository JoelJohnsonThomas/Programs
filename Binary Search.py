def bsearch(alist,item):
    first =0
    last =len(alist)-1
    found =False
    while first<=last and not found:
        mid =(first+last)//2
        if alist[mid]==item:
            found =True
            print("Element Found At",mid)
        else:
            if item<mid:
                mid =mid-1
                print("Element Found At", mid)
            else:
                mid =mid+1
                print("Element Found At", mid)
        return found
a=[]
n=int(input("Enter The Upper Limit:"))
for i in range(0,n):
    e=int(input("Enter The Elements:"))
    a.append(e)
x =int(input("Enter The Element To Be Searched:"))
bsearch(a,x)
