s,t=list(map(int,input().split()))
alo,olo=list(map(int,input().split()))
apples,oranges=list(map(int,input().split()))
anum=list(map(int,input().split()))
onum=list(map(int,input().split()))

totalapple=0
totalorange=0

for i in range(len(anum)):
  location1=alo+anum[i]
  if s<=location1<=t:
    print(totalapple+1)
for i in range(len(onum)):
  location2=olo+onum[i]
  if s<=location2<=t:
    print(totalorange+1)