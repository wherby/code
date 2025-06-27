# https://leetcode.cn/problems/longest-subsequence-repeated-k-times/?envType=daily-question&envId=2025-06-27
# 利用dfs维护字典序最大值，遍历所有可能的答案
from collections import Counter
from collections import defaultdict,deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def check(s1,k):
            m = len(s1)
            i = 0 
            for c in s :
                if c == s1[i]:
                    i +=1
                if i == m:
                    k -=1
                    i = 0 
                if k == 0:
                    return True 
            return False
             
        c = Counter(s)
        ks = [key for key,v in c.items() if v >=k]
        ks.sort()
        que = deque([""])
        ans = ""
        while que:
            cand = que.popleft()
            for c1 in ks:
                tmp= cand + c1 
                if check(tmp,k):
                    ans = tmp 
                    que.append(tmp)
        return ans