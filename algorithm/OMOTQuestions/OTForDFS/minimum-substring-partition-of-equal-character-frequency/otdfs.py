# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/submissions/559179066/?envType=daily-question&envId=2024-08-28
# 超出时间限制 因为 verify的时候多用了时间
from functools import cache

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        ls = [[0]*26 for _ in range(n+1)]
        for i ,a in enumerate(s):
            ls[i+1] = list(ls[i])
            ls[i+1][ord(a) - ord('a')] +=1
        
        @cache
        def verify(a,b):
            ret = [x-y for x,y in zip(ls[b],ls[a])]
            st = set()
            for a in ret:
                if a >0:
                    st.add(a)
            #print(a,b,ret,st)
            return len(st) == 1
        @cache
        def dfs(idx):
            if idx ==0: 
                return 0
            ret = 10**10 
            for i in range(idx):
                if verify(i,idx):
                    ret = min(ret,1+dfs(i))
            return ret
        return dfs(n)

s ="pvpvlsmojtmkmdbpseorfiibfdmlbffxxnlpnjiqoovvzzzzzzzzzzzzzzzkkkhiknkihkkkkikhkkknknhinkkkllkkmllkllmlmlmuuuuuuuuuuuuuuuskkuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuyyyyyiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxjkklkjlkipvstfuuistpvvdiutodqgkqqfkoksssiisusomdpsiutgtdstqsfqmuqfiuiqitgomvspkfkmugodsqsuttvpqguistsqmoonnnnonoooonnonooonnononnonnonooononnonnoonnoonnonnonoononowpppoooopppoopoppoopakjgqegsnarxkfzdjvbjecpkldfcabaauyyyxxxuutxxyutyxuxxuutuxutuxxtutxyxtxxxxuxxxuxuyvvvvvvvvvvvvvmnmmmmnmmnnmmnnmnmmnmnmmnnmmmnmmmmmnnmnmmnnmmmmmnnmnmmmnmmmmmnmmnmnmmmmmzzzzzzjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnnmmpnqqqqpppnqqmqmqhhhhhhklkjhjyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyffffffooooooeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeenn"
re= Solution().minimumSubstringsInPartition(s)
print(re)