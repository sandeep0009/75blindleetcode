
#brute force
# def threeSum(nums):

#     nums.sort()
#     result=set()
#     n=len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     result.add(tuple(sorted(nums[i],nums[j],nums[k])))
    
#     return list(result)


def threesum(nums):
    n=len(nums)
    nums.sort()
    ans=[]
    for i in range(0,n):
        if i>0 and nums[i]==nums[i-1]:continue
        j=i+1
        k=n-1
        while j<k:
            sum=nums[i]+nums[j]+nums[k]
            if sum<0:
                j+=1
            elif sum>0:
                k-=1
            else:
                
                ans.append([nums[i], nums[j], nums[k]])
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:j+=1
                while j<k and nums[k]==nums[k-1]:k-=1
    
    return ans

nums = [-1,0,1,2,-1,-4]

print(threesum(nums))