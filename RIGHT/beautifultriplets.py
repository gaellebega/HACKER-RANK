from collections import Counter
arr=list(map(int,input().split()))
d=int(input())

m=Counter(arr)
for num in arr:
  if m[num+d]==m[num+d+d]:
    count+=1
print(count)   