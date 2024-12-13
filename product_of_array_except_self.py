def product_of_arr(arr):
    n=len(arr)
    suffix=[1]*n
    prefix=[1]*n
    output=[1]*n
    for i in range(1,n):
        prefix[i]=prefix[i-1]*arr[i-1]

    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]*arr[i+1]

    for i in range(n):
        output[i]=prefix[i]*suffix[i]

    

    return output




arr=[1,2,3,4]

print(product_of_arr(arr))