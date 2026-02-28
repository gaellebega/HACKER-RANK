from collections import Counter
n,m=list(map(int,input().split()))
magazine=input().split()
magazine_count=Counter(magazine)
ransom=input().split()
ransom_count=Counter(ransom)
for word in ransom_count:
  # if  ransom_count[word]>magazine_count[word]:
  if  ransom_count[word]>magazine_count.get(word,0):
    print("No")
    break
else:
   print("Yes")    