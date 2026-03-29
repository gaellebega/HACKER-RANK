 left=0
right=1
n=len(arr)
while(right<n):
 diff=arr[right]-arr[left]
 min_diff=min(diff,min_diff)
 return min_diff