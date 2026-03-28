from collections import Counter
def anagrams(s):
  if len(s)%2!=0:
    return -1
  first=Counter()
  last=Counter()
  middle=len(s)//2
  for i in range(middle):
    first[s[i]]+=1
  for j in range(middle,len(s)-1):
      last[s[j]]+=1
  changes=0    
  # ho many changes letters in first are missing in last
  for ch in first:
    if first[ch]>last[ch]:
        changes+=first[ch]-last[ch] 
  return changes
