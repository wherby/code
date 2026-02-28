# https://leetcode.cn/problems/minimum-operations-to-equalize-binary-string/description/?envType=daily-question&envId=2026-02-27
# 维护操作的范围，贪心计算下次可能的范围值。

from sortedcontainers import SortedDict,SortedList

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        cnt=0 
        for a in s:
            if a =="0":
                cnt +=1
        sl = [SortedList(),SortedList()]
        m = len(s)
        for i in range(len(s)+1):
            sl[i%2].add((i,m-i))
        cand = [(cnt,m-cnt,0)]
        sl[cnt%2].remove((cnt,m-cnt))
        for _ in range(m*2):
            tmp = []
            for z,o,turn in cand:
                if z ==0:
                    return turn 
                t = (z+k)%2
                rm = []
                zm,om = min(z,k),min(o,k)
                zf = z-zm +(k-zm)
                zt = z+om -(k-om)
                idx = sl[t].bisect_left((zf,0))
                
                for i in range(idx,len(sl[t])):
                    nz,no = sl[t][i]
                    if nz > zt:
                        break
                    rm.append((nz,no))
                for a in rm:
                    sl[t].remove(a)
                    tmp.append((a[0],a[1],turn+1))
            cand = tmp
        return -1