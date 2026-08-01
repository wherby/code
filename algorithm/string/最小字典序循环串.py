# https://leetcode.cn/contest/weekly-contest-511/problems/minimum-number-of-string-groups-through-transformations/description/
# 另一种写法： algorithm/string/最小表示法.py
# 比较跳跃的时候，是排除了k个一定不符合的起点，一共有2*n 个起始点，平均每次操作排除一个位置 

from typing import List, Tuple, Optional
class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        def getMin(s):
            n = len(s)
            ss = s+s 
            i,j,k = 0,1,0 
            while i <n and j <n and k<n:
                diff = ord(ss[i+k]) -ord(ss[j+k])
                if diff ==0:
                    k +=1
                else:
                    if diff>0:
                        i += k+1
                    else:
                        j +=k+1
                    if i == j:
                        j+=1
                    k = 0 
            start = min(i,j)
            return ss[start:start+n]
        dic = {}
        for w in words:
            eq= "".join([w[i] for i in range(0,len(w),2)])
            oq = "".join([w[i] for i in range(1,len(w),2)])
            eq = getMin(eq)
            oq = getMin(oq)
            dic[eq+oq] =1 
        return len(dic)