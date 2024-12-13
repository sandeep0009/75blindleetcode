def buy_sell(arr):
    mini=arr[0]
    profit=0
    n=len(arr)
    for i in range(n):
        cost=mini-arr[i]
        profit=max(profit,cost)
        mini=min(mini,arr[i])
    

    return profit-mini



arr=[7,1,5,3,6,4]

print(buy_sell(arr))
