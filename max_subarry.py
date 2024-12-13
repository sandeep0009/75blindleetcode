def max_subarry(nums):
    n=len(nums)
    maxi=nums[0]
    sum=0
    for i in range(0,n):
        sum+=nums[i]
        maxi=max(sum,maxi)
        if sum<0:

            sum=0

    return maxi


nums=[-2,1,-3,4,-1,2,1,-5,4]

print(max_subarry(nums))