def lbseq(arr): 
    n = len(arr) 
    lis = [1 for i in range(n+1)] 
    for i in range(1 , n): 
        for j in range(0 , i): 
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
                lis[i] = lis[j] + 1
    lds = [1 for i in range(n+1)] 
      
 
    for i in reversed(range(n-1)): 
        for j in reversed(range(i-1 ,n)):
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1 
  
    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n): 
        maximum = max((lis[i] + lds[i]-1), maximum) 
      
    return maximum 
  
arr =  [0 , 8 , 24, 12, 2, 10 , 6 , 14 , 1 , 9 , 15 , 13, 
        3, 9 , 60 , 15] 
print ("Length of LBS is",lbseq(arr)) 
  
