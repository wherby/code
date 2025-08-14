from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList
def getNoInvidSubArray(ls, invaidPair):
    dic= {}
    for i,a in enumerate(ls):
        dic[a] = i 
    dic2 = defaultdict(lambda : -1)
    for a,b in invaidPair:
        ai,bi = dic[a],dic[b]
        if ai > bi:
            ai,bi = bi,ai 
        dic2[bi] = max(dic2[bi],ai)
    cnt = 0 
    l = -1
    for i,a in enumerate(ls):
        l = max(l,dic2[i])
        cnt += i-l 
    return cnt
                




ls = [9,7,2,3,1,4,6,5,8]
pair = [[1,6],[5,4],[2,7]]
re = getNoInvidSubArray(ls,pair)
print(re)





