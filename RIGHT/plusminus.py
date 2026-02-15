n=int(input())
arr=list(map(int,input().split()))
pos=nega=zero=0
size=len(arr)
for i in arr:
 if i>0:
  pos+=1

 elif i<0:
  nega+=1
  
 else:
  zero+=1

first=pos/size
second=nega/size
third=zero/size
print(f"{first:.6f}")  
print(f"{second:.6f}")
print(f"{third:.6f}")
