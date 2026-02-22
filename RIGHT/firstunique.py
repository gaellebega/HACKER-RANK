from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # mapping character with the count
        # zero bcz the default value of the int is 0
        count=defaultdict(int) 
        for ch in s:
           count[ch]+=1   
        #    to get thte index and the character at the same time
        for i,ch in enumerate(s):
            if count[ch]==1:
                return i
        return -1
     