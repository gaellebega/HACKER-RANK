n=int(input())
arr=list(map(int,input().split()))

first=second=third=0
for i in range(len(arr)):
  first=sum(arr[1:])
  second=sum(arr[2:9])
  third=sum(arr[:-1])
  together=first+second+third
print(together) 

  