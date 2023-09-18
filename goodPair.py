def goodpair(nums:list[int])->int:
     i=0
     j=len(nums)-1
     count=0
     while(i<j):
          for i in range(0,len(nums)):
               for j in range(len(nums)-1, -1, -1):
                    if nums[i]==nums[j]:
                         count +=1
          return count
nums=[1,2,3,1,1,3]
res=goodpair(nums)
print(res)
