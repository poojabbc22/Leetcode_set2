def tarit(nums:list[int],target:int)->int:
    unique={}
    n=len(nums)
    nums.sort()
    for i in range(n):
        diff=target-nums[i]
        unique.update({diff: nums[i]})
    for k,v in unique.items():
        if all(v < value for key, value in unique.items() if key != k):
            print(v)
nums=[-1,2,5,0,3,6]
target=8
res=tarit(nums, target)
print(res)