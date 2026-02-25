x1,v1,x2,v2=list(map(int,input().split()))

distance_moves=v1*x2
target_moves=distance_moves//v1
new=v1*v2
if new*target_moves!=distance_moves:
  print("Yes")
else:
  print("No")

