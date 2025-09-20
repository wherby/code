from typing import List, Tuple, Optional


class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <=4:
            return [] 
        ret = [[0,1],[2,3],[0,4],[1,2],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[2,0],[3,1],[4,0],[2,1],[4,3],[1,0],[3,2],[4,1],[3,0],[4,2]]
        cur = 5
        while cur <n:
            tmp = list(ret)
            nxt= cur +1 
            toAdd= []
            for i in range(nxt):
                toAdd.append((i,cur))
                toAdd.append((cur,i))
            for a,b in toAdd:
                m = len(tmp)
                for i in range(m):
                    c,d = tmp[i]
                    e,f = tmp[i-1]
                    if len(set([a,b,c,d])) ==4 and len(set([a,b,e,f])) == 4: 
                        tmp = tmp[:i] + [[a,b]] + tmp[i:]
                        break
            ret = tmp
            cur +=1

        return ret


re =Solution().generateSchedule(6)
print(re)


a = [[3,6],[0,1],[4,6],[2,3],[1,6],[0,4],[6,3],[1,2],[0,6],[3,4],[6,1],[0,2],[6,4],[1,3],[6,0],[2,4],[5,6],[0,3],[2,6],[1,4],[6,5],[2,0],[3,1],[6,2],[4,0],[2,1],[4,3],[1,0],[3,2],[4,1],[3,0],[4,2]]
b = [[0,1],[2,3],[4,5],[0,2],[1,3],[5,4],[0,3],[1,2],[0,4],[1,5],[2,4],[3,5],[1,0],[2,5],[3,4],[0,5],[1,4],[3,2],[4,0],[2,1],[5,3],[2,0],[3,1],[4,2],[5,0],[4,1],[3,0],[5,1],[4,3],[5,2]]
a.sort()
b.sort()
print(a)
print(b)