arr=list(map(int,input().split()))
k=int(input())
for i in range(k):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min] :
          min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr[k-1])
        
