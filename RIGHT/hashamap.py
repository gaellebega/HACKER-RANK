frequ={}
nums=[1,2,3,1,2,3,3]
for num in nums:
  if num in frequ:
    frequ[num]+=1
  else:
    frequ[num]=1  
print(frequ)    