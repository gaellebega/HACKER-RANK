x1,v1,x2,v2=list(map(int,input().split()))
if v1==v2:
  if x1==x2:
    print("Yes")
  else:
    print("No")
else:    
  n=(x1-x2)/(v2-v1)
  first=x1+n*v1
  second=x2+n*v2
  if first==second:
    print("Yes")
    
  else:
    print("No")