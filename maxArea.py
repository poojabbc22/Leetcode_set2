def maxArea(height:list[int])->int:
    l,r=0,len(height)-1
    res=0
    while l<r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l]<height[r]:
            l+=1
        elif height[r] <= height[l]:
            r-=1
    return res
height=[1,8,6,2,3,7]
res=maxArea(height)
print(res)
