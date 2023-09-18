def candy(candies:list[int],extra:int)->bool:
     extracandy=[]
     result=[]
     n=len(candies)
     for i in range(n):
          extracandy.append(candies[i]+extra)
     print(extracandy)
     for i in range(n):
          for j in range(i+1,n):

               cond=any(extracandy[i] >=extracandy[j])
               result.append(cond)

     return result

candies=[1,3,8,9,1]
extra=4
res=candy(candies,extra)
print(res)
