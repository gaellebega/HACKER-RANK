# sticks=list(map(int,input().split()))
def make_sticks(sticks):
  sticks.sort()
  n=len(sticks)
  right=n-1
  middle=n-2
  left=n-3

  while(left>=0):
    if sticks[left]+sticks[middle]>sticks[right]:
      return [sticks[left],sticks[middle],sticks[right]]
    left-=1
    middle-=1
    right-=1
  return [-1]  
print(make_sticks([11133]))