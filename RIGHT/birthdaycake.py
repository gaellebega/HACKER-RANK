n=int(input())
cake_height=list(map(int,input().split()))
new=max(cake_height)
print(cake_height.count(new))