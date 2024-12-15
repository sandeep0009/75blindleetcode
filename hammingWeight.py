def hammingWeight(num):
    res=0
    while num!=0:
        res+=num%2
        num=num>>1
    

    return res



print(hammingWeight(11))