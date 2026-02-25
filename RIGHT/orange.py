# 7,11
s,t=list(map(int,input().split()))
# 5,15
appleposi,orangepos=list(map(int,input().split()))
# 3,2
applenum,orangenum=list(map(int,input().split()))
# [-2,2,1]
appledis=list(map(int,input().split()))
# [5,-6]
orangedis=list(map(int,input().split()))
# check which fruits lands 
totalapples=0
totaloranges=0
# len cz am gonna need the index
for i in range(len(appledis)):
  location1=appleposi+appledis[i]
  if s<=location1<=t:
    totalapples+=1
for i in range(len(orangedis)):
  location2=orangepos+orangedis[i]
  if s<=location2<=t:
    totaloranges+=1
print(totalapples)
print(totaloranges)    


 