n=int(input())
arr=list(map(int,input().split()))
unique=set(arr)
for num in arr:
  if  num in unique:
     weneed=arr.count(num)
print(weneed)    
