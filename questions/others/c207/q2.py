class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def verify(idx):
            res=[]
            start =0
            for i in range(n-1):
                if (idx & (1<<i)) != 0:
                    res.append(s[start:i+1])
                    start = i+1
            res.append(s[start:])
            #print(res)
            if len(res) == len(set(res)):
                return len(res)
            return 0
        mx = 0
        for i in range((1<<(n-1))):
            mx=max(mx, verify(i))
        return mx

re =Solution().maxUniqueSplit("ababccc")
print(re)
            
                     
