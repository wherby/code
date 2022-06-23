from itertools import accumulate
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2062017/C%2B%2B-prefix-%2B-monotonic-stack-O(N)-solution-with-thought-process
# https://leetcode.cn/contest/weekly-contest-294/problems/sum-of-total-strength-of-wizards/

def nextSmall(A):
    # next small on the right
    n = len(A)
    right = [n]*n
    stack=[]
    for i in range(n):
        while stack and A[stack[-1]] >= A[i]:
            right[stack.pop()] = i 
        stack.append(i)
    
    # next small on the left
    left = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and A[stack[-1]] > A[i]:
            left[stack.pop()] = i 
        stack.append(i)
    return (left,right)
class Solution:
    def totalStrength(self, A) -> int:
        n = len(A)
        mod = 10**9+7
        left,right = nextSmall(A)
        res =0
        acc = list(accumulate(accumulate(A), initial = 0))
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += A[i] * (racc * ln - lacc * rn)
        return res%mod
        
re = Solution().totalStrength([5,4,6])
print(re)

## [1,5] ,2

# pre[2]-pre[1]
# pre[3]-pre[1]
# pre[4]-pre[1]
# pre[5]-pre[1]
# pre[2]-pre[2]
# pre[3] -pre[2]
# pre[4] -pre[2]
# pre[5]-pre[2]

## (pp[r] -pp[i]) * (i-l)
## (pp[i] - pp[l]) *(r-i) 