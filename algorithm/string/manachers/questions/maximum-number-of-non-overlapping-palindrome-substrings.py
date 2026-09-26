# https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/?envType=daily-question&envId=2026-09-15


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i]) # Z[2*center -i]是 i 关于center的对称点， 因为在[left, right]上对称，则 对称点的对称性是对称的
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:1]
        ls= manachers(s)
        cnt = 0 
        n =len(ls)
        lst = -1 
        for i,a in enumerate(ls):
            cstart = (i - a+1) // 2
            if a -max(lst-cstart,0)*2 >=k:
                cnt +=1
                min_len = k + (a - k) % 2
                lst = (i + min_len + 1) // 2
        return cnt

re =Solution().maxPalindromes("zqzogfurlfmrnlffuipuupidkfhkggkhdrzezghwziopoinnsdkwkymhygonbiizmmmmzjhmyczzlz",2)
print(re)