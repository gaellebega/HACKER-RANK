n=int(input())
line1=list(map(int,input().split()))
line2=list(map(int,input().split()))
line3=list(map(int,input().split()))
for _ in range(len(n)):
  first=line1[0]+line2[1]+line3[2]
  second=line3[0]+line2[1]+line1[2]
  difference=second-first
print(difference)