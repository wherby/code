# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/submissions/559179066/?envType=daily-question&envId=2024-08-28
# 通过 
from functools import cache
from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**4)
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        ls = [[0]*26 for _ in range(n+1)]
        for i ,a in enumerate(s):
            ls[i+1] = list(ls[i])
            ls[i+1][ord(a) - ord('a')] +=1
        

        @cache
        def dfs(idx):
            #print(idx)
            if idx ==-1: 
                return 0
            ret = 10**10 
            c= defaultdict(int)
            for i in range(idx,-1,-1):
                c[s[i]] +=1
                if len(set(c.values())) ==1:
                    ret = min(ret,1+dfs(i-1))
            return ret
        return dfs(n-1)

s ="pvpvlsmojtmkmdbpseorfiibfdmlbffxxnlpnjiqoovvzzzzzzzzzzzzzzzkkkhiknkihkkkkikhkkknknhinkkkllkkmllkllmlmlmuuuuuuuuuuuuuuuskkuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuyyyyyiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxjkklkjlkipvstfuuistpvvdiutodqgkqqfkoksssiisusomdpsiutgtdstqsfqmuqfiuiqitgomvspkfkmugodsqsuttvpqguistsqmoonnnnonoooonnonooonnononnonnonooononnonnoonnoonnonnonoononowpppoooopppoopoppoopakjgqegsnarxkfzdjvbjecpkldfcabaauyyyxxxuutxxyutyxuxxuutuxutuxxtutxyxtxxxxuxxxuxuyvvvvvvvvvvvvvmnmmmmnmmnnmmnnmnmmnmnmmnnmmmnmmmmmnnmnmmnnmmmmmnnmnmmmnmmmmmnmmnmnmmmmmzzzzzzjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnnmmpnqqqqpppnqqmqmqhhhhhhklkjhjyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyffffffooooooeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeenn"
re= Solution().minimumSubstringsInPartition(s)
print(re)