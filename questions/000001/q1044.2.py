import random
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def rollingHashDoubleHash(arr, m):
            # 生成两个进制
            a1, a2 = random.randint(26, 100), random.randint(26, 100)
            # 生成两个模
            mod1, mod2 = random.randint(10**9+7, 2**31-1), random.randint(10**9+7, 2**31-1)
            n =len(arr)
            aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
            h1, h2 = 0, 0
            for i in range(m):
                    h1 = (h1 * a1 + arr[i]) % mod1
                    h2 = (h2 * a2 + arr[i]) % mod2
            seen = {(h1, h2)}
            for start in range(1, n - m + 1):
                h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
                h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + m - 1]) % mod2
                # 如果重复，则返回重复串的起点
                if (h1, h2) in seen:
                    return start
                seen.add((h1, h2))
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

re = Solution().longestDupSubstring(s = "abcd")
print(re)


            
