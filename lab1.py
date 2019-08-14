def sqrt(n) :
 first,last=0,n
 if n<0 :
  return"Imaginary"
 while(first<=last) :
  mid=(int(first+last)/2)
  if mid*mid==n :
   ans=mid
   break
  elif mid*mid<n :
   first=mid+1
   ans=mid
  else :
   last=mid-1
 return ans
x=int(input("Enter value of x:"))
print(sqrt(x))
