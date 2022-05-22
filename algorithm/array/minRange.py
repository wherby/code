#https://zhuanlan.zhihu.com/p/103562972
class Solution:
    def sumSubarrayMins(self, A) -> int:
        MOD = 1e9 + 7
        n = len(A)
        pre = [0] * n
        nxt = [0] * n
        sp = []
        sn = []
        for i in range(n):
            while len(sp) != 0 and A[sp[-1]] >= A[i]:
                sp.pop()
            pre[i] = i + 1 if len(sp) == 0 else i - sp[-1]
            sp.append(i)
        
        for i in range(n-1, -1, -1):
            while len(sn) != 0 and A[sn[-1]] > A[i]:
                sn.pop()
            nxt[i] = n - i if len(sn) == 0 else sn[-1] - i
            sn.append(i)
        print(pre,nxt)
        res = sum([pre[i] * nxt[i] * A[i] for i in range(n)]) % MOD
        return int(res)
    
A = [2,1,3,2,1,4,2,1,4]
re = Solution().sumSubarrayMins(A)
print(re)