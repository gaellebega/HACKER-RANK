from typing import List
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    new_string=[]    
    for str in range(len(strs)-1):
        if set(strs[str].split())==set(strs[str+1].split()):
            new_string.append([strs[str],strs[str+1]])
        else:
            new_string.append([strs[str+1]])  
    return new_string        
      
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))