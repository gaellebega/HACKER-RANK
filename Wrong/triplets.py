alice_points=list(map(int,input().split()))
bob_points=list(map(int,input().split()))
count=0
# when you want to get the index also you got use the length
for n in range(len(alice_points)):
  if alice_points[n] > bob_points[n] or alice_points[n]<bob_points[n]:
    # this is to be able to update the variable
    count+=1
  else:
    break
print(count)  
  