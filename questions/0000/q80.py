from sortedcontainers import SortedDict,SortedList
from collections import defaultdict
class Solution:
    def rectangleArea(self, rectangles) -> int:
        ls =[]
        st =SortedList()
        dic=defaultdict(list)
        for a,b,c,d in rectangles:
            dic[a].append((d,-1,1))
            dic[a].append((b,1,1))
            dic[c].append((d,-1,-1))
            dic[c].append((b,1,-1))
        sm = 0
        keys = sorted(dic.keys())

        lastIdx =0 
        mod = 10**9+7
        ttm =0
        for k in keys:
            dic2 = defaultdict(list)
            for a,b,c in dic[k]:
                if c ==1:
                    st.add((a,b))
                else:
                    st.remove((a,b))
            for a,b in st:
                dic2[a].append(b)
            acc =0
            last =0
            tm =0 
            #print(dic2,st)
            for k2 in sorted(dic2.keys()):
                if acc >0:
                    tm += k2 - last
                last = k2
                for b in dic2[k2]:
                    acc += b 
            sm += ttm * (k-lastIdx)
            lastIdx = k
            ttm = tm
            sm = sm%mod
            #print(sm,k,ttm,lastIdx)
        return sm

re = Solution().rectangleArea([[25,20,70,27],[68,80,79,100],[37,41,66,76]])
#re = Solution().rectangleArea( [[0,0,2,2],[1,0,2,3],[1,0,3,1]])
print(re)

        