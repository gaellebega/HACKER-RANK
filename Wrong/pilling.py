
arr=list(map(int,input().split()))
def make_pilling(unique):
 new_num=sorted(arr)
 unique=set(new_num)
 for i in len((unique)-1):
    if all(unique[i]>unique[i+1]):
     print("Yes")
    else:
     print("No")
 return unique
# print(make_pilling(unique))
