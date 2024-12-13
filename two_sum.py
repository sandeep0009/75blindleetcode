def two_sum(nums,target):
    num_map={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in num_map:
            return [num_map[diff],i]
        num_map[n]=i
    
    return []



nums=[2,3,4,5,6]
target=9


two_sum(nums,9)

