def contains_duplicate(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            return True
    return False


arr=[1,2,3,1]

print(contains_duplicate(arr))
        