class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        n= len(str(low))
        m = len(str(high))
        ls = [i for i in range(1,9)]
        cand =[]
        for le in range(n,m+1):
            for start in range(1,11-le):
                cnt =0
                for j in range(le):
                    cnt = cnt * 10+ (start +j)
                cand.append(cnt)
        re =[]
        for c in cand:
            if c >= low and c <= high:
                re.append(c)
        re.sort()
        return re

re = Solution().sequentialDigits(low = 1000, high = 13000)
print(re)

