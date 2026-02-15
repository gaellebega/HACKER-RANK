numbers=list(map(int,input().split()))
total=0
def minmaxSum(arr):
  # numbers=[1,2,3,4,5] min//10 max 14
  # how it is done
  for num in range(6):
    minsum=total+len(numbers)-numbers[-1]
    maxsum=total+len(numbers)-numbers[0]
  return {f"{minsum} {maxsum}"}
minmaxSum()
