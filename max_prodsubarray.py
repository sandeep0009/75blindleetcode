def max_prodsubbarray(nums):
    prefix=1
    suffix=1
    n=len(nums)
    maxi=0

    for i in range(0,n):
        if prefix==0:prefix=1
        if suffix==0:suffix=1

        prefix=prefix*nums[i]
        suffix=suffix*nums[n-i-1]

        maxi=max(maxi,max(prefix,suffix))


    return maxi



nums=[2,3,-2,4]

print(max_prodsubbarray(nums))