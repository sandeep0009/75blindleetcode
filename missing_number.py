def missing_number(nums):
    n=len(nums)
    res=0

    for i in range(n+1):
        res^=i
    for num in nums:
        res^=num
    return res


print(missing_number([3,0,1]))