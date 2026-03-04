nums=list(map(int,input().split()))
k=int(input())    

def make_pairs(nums,k):
#must be created inside of the function
    indexes=[]
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
            difference=nums[j]-nums[i]
            if  difference==k:
                indexes.append((j,j))
    return indexes
print(make_pairs(nums,k))  
