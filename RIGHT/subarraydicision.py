import math
import os
import random
import re
import sys
s=list(map(int,input().split()))
d=int(input())
m=int(input())
count=0
n=len(s)
for i in range(0,n-m+1):
  if sum(s[i:i+m])==d:
     count+=1
print(count)  
  