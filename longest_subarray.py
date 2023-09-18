def longssub(word:str)->str:
    longsub=""
    l,r=0,len(word)-1
    while(l<r):
        for char in word:
            if char[l]==char[r]:
                l+=1
            longsub+=char
        return longsub
word = "abcabcbb"
res = longssub(word)
print(res)