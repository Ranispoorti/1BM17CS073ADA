arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        c=c+1
        if arr[j]<arr[min] :
          min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr)
print(c)
