arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        c=c+1
        if arr[j]>arr[j+1] :
           arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
print(c)
