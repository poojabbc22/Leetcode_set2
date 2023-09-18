def dotsenate(senate:str)->str:
    R,D=deque(),deque()
    senate=list(senate)
    for i,c in enumerate(senate):
        if c=='R':
            R.append(i)
        else:
            D.append(i)

    while D and R:
        dTurn=D.popleft()
        rTurn=R.popleft()

        if rTurn<dTurn:
            R.append(dTurn+len(senate))
        else:
            D.append(rTurn+len(senate))

    return 'Radiant' if R else 'Dire'

senate = "RDD"
result = dotsenate(senate)
print(result)