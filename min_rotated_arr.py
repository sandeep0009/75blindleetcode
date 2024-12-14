def min_in_rotated_sorted_array(nums):
    n=len(nums)
    high=n-1
    low=0
    ans=float("inf")

    while low<=high:
        mid=(low+high)//2
        if nums[low]<=nums[mid]:
            ans=min(ans,nums[low])
            low=mid+1

        else:
            
            ans=min(ans,nums[high])
            high=mid-1

    return ans


nums = [3,4,5,1,2]

print(min_in_rotated_sorted_array(nums))