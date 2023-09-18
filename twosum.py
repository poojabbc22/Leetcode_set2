def twosum(nums:list[int],t:int)->list[int]:
    prevmap={}  #index,value
    for i , n in enumerate(nums):
        diff=t-n
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[n]=i
    return
nums=[2,3,0,1,7]
t=8
result=twosum(nums,t)
print(result)