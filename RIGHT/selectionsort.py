arr=[1,5,7,2,3,90]
n=len(arr)
for i in range(0,n):
  for j in range(i+1,n):
    if arr[j]<arr[i]:
      arr[j],arr[i]=arr[i],arr[j]
print(arr)    