from collections import defaultdict,deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        step,n = 0, len(s1)
        q,vist =deque([(s1,0,0)]),{s1}
        while q:
            st,i,step = q.popleft()
            if st == s2:
                return step
            while i <n and st[i] == s2[i]:
                i +=1
            for j in range(i+1,n):
                if st[j] == s2[i] != s2[j]:
                    t = list(st)
                    t[i],t[j] = t[j],t[i]
                    t  = "".join(t)
                    if t not in vist:
                        vist.add(t)
                        q.append((t,i+1,step+1))
            

re = Solution().kSimilarity(s1 = "abc", s2 = "bca")
print(re)