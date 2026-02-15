numbers=list(map(int,input().split()))
def miniMaxSum(arr):
  arr.sort()
  minSum=sum(numbers[:-1])
  maxSum=sum(numbers[1:])
  print (minSum,maxSum)
miniMaxSum(numbers)  
 

