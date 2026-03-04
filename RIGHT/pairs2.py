n,k=map(int,input().split())
nums=list(map(int,input().split()))

def make_pairs(nums,k):
  set_nums=set(nums)
  count=0
  for num in nums:
    diff=num-k
    if diff==set_nums:
      count+=1
  return count 
print(make_pairs(nums,k))     

      