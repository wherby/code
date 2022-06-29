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
        print(pre,nxt,)
        res = sum([pre[i] * nxt[i] * A[i] for i in range(n)]) % MOD
        return int(res)

#给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
#由于答案可能很大，因此返回答案模 10^9 + 7。
#示例1
#输入：
#[3,1,2,4]
#输出：
#17
#解释：
#子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
#最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

# 求子数组的最小值之和
# pre,nxt 表示当前元素能向前，向后影响的子数组的长度(包括自己)
A = [2,1,3,2,1,4,2,1,4]
re = Solution().sumSubarrayMins(A)
print(re)