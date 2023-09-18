def subarray(nums:list[int])->list[int]:
    maxsub=nums[0]
    cursum=0
    for n in nums:
        if cursum<0:
            cursum=0
        cursum+=n
        maxsub=max(maxsub,cursum)
    return maxsub
nums=[2,1,-7,-9,3,7,-1,0,4,5]
res=subarray(nums)
print(res)
