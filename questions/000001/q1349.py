from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m,n = len(seats), len(seats[0])

        @cache
        def dfs(i,pre):
            if i == m:
                return 0 
            ret = 0
            def verify(state,prestate, idx):
                ps = bin(prestate + (1<<20))[-n:]
                cs = bin(state+ (1<<20))[-n:]
                for i in range(n):
                    if cs[i] == "1" and seats[idx][i] == "#":
                        return False
                    if i >0 and cs[i]=="1" and cs[i-1] =="1":
                        return False
                    if i>0 and cs[i] == "1" and ps[i-1]=="1":
                        return False
                    if i <n-1 and cs[i] =="1" and ps[i+1] == "1" :
                        return False
                return True
            for j in range(1<<n):
                if verify(j,pre,i):
                    ret = max(ret,bin(j).count("1") + dfs(i+1,j))
            return ret
        return dfs(0,0)
    





re= Solution().maxStudents([["#",".",".",".","#"],
              [".","#",".","#","."],
              [".",".","#",".","."],
              [".","#",".","#","."],
              ["#",".",".",".","#"]])
print(re)