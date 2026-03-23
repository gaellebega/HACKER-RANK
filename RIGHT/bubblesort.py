arr=[3,2,1]
n=len(arr)
count=0
for i in range(n):
  for j in range(i+1,n):
    if arr[i]>arr[j]:
      arr[i],arr[j]=arr[j],arr[i]
      count+=1
counted=f"Array is sorted un {count} swaps."
first=f"First Element:{arr[0]}"
second=f"Last Element:{arr[-1]}"
print(counted)
print(first)
print(second)

