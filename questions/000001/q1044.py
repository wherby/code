import random
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def rollingHashDoubleHash(arr, m):
            # use mod =2**64 k =131 or 13331
            a1 = 131
            mod1 = 2**64
            n =len(arr)
            aL1= pow(a1, m, mod1)
            h1 = 0
            for i in range(m):
                h1 = (h1 * a1 + arr[i]) % mod1
            seen = {h1:1}
            for start in range(1, n - m + 1):
                h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
                # 如果重复，则返回重复串的起点
                if h1 in seen:
                    return start
                seen[h1]=1
            # 没有重复，则返回-1
            return -1
        arr =list(map(lambda x: ord(x)- ord('a'),s))
        l = 0 
        r = len(arr)
        mxl =-1
        startM =-1
        while l<r:
            mid = (l+r+1)>>1
            start = rollingHashDoubleHash(arr,mid)
            if start != -1:
                l = mid 
                l=mid
                if mid > mxl:
                    mxl = mid
                    startM = start
            else:
                r = mid-1
        if l == 0:
            return ""
        return s[startM:startM+l]

re = Solution().longestDupSubstring(s = "banana")
print(re)


            
