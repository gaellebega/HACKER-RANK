x1,v1,x2,v2=list(map(int,input().split()))
if x1==x2:
  if v1==v2:
    print("Yes") 
  else:
    print("No")
else:
   jumps=(x2-x1)/(v1-v2)
  #if the jumps are greater than 0 and the jumps are not float
   if jumps>=0 and jumps==int(jumps):
     print("yes")
   else:
     print("No")

