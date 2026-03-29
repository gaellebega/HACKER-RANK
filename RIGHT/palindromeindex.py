def palindrome_index(s):
  if s==s[::-1]:
    return -1
  right=len(s)-1
  left=0
  while(left<right):
    if s[right]==s[left]:
      right-=1
      left+=1
    else:
      if s[left+1:right+1]==s[left+1:right+1][::-1]:
        return left
      elif s[left:right]==s[left:right][::1]:
        return right
    return -1
  return -1    

