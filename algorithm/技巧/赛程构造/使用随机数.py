# 使用shuffle 函数生成随机序列
# 有了随机序列的同时，也需要greedy 寻找可能的下一个可能的排列，才能生成答案，如果只是shuffle随机序列的话，是不可能得到合法的答案的。
from typing import List, Tuple, Optional
from random import shuffle

class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <=4:
            return [] 
        cand = []
        for i in range(n):
            for j in range(n):
                if i ==j : continue
                cand.append((i,j))
        isG= False
        m = len(cand)
        while isG == False:
            shuffle(cand)
            candCp= list(cand)
            ans = []
            for _ in range(m):
                fd = False
                for i in range(len(candCp)):
                    a,b = candCp[i]
                    if len(ans) ==0  or (len(set([a,b,ans[-1][0],ans[-1][1]]))==4):
                        fd = True 
                        ans.append((a,b))
                        candCp.pop(i)
                        break
                if fd == False:
                    break
            if len(ans) == m:
                isG = True
        return ans


re =Solution().generateSchedule(6)
print(re)

