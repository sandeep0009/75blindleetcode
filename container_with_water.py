def maxArea(height):
    n=len(height)
    low=0
    right=n-1
    max_area=0
    while low<right:
        max_area=max(max_area,(right - low)* min(height[low],height[right]))
        if height[low]<height[right]:
            low+=1
        else:
            right-=1
    
    return max_area



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

