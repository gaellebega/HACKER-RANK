frequ={}
for str in strs:
  count=[0]*26
  for c in  str:
   count[ord(c)-ord("a")]+1
   frequ[tuple(count)].append(str)  
return frequ.values()