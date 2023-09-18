
def validparen(s:str):
     sli=list(s)
     s=len(sli)
     for i in range(s):
         for j in range(i+1,s):
             if sli[i]==sli[j]:
             elif sli[i]=='' or sli[j]=='':
                 continue
             else:
                 return False
     return sli
s="() {}"
res=validparen(s)
print(res)