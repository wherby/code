

def rangeGreedy(ranges):
    ranges.sort()
    pos = -10**9
    ans =0
    for i in range(len(ranges)):
        l,r = ranges[i]
        if pos < l:
            ans +=1
            pos = r
        else:
            pos = min(r,pos)
    return ans





ranges =[[1,4],[2,10],[5,8],[10,12],[1,3]]
re = rangeGreedy(ranges)
print(re)