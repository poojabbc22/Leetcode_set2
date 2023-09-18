def uniquefile(nums:list[str])->list[str]:
    count=0
    res=[]
    n=len(nums)
    for word in range(n):
        for letter in range(word+1,n):
            if nums[word]==nums[letter]:
                count+=1
                newname = f"{nums[letter]}({count})"
                print(newname)
                res.append(newname)
                nums[letter] = newname

    return res

nums= ["gta","gta(1)","gta1","gta","gta","avalon"]
res=uniquefile(nums)
print(nums)
