class Solution:
    def makeFancyString(self, s: str) -> str:
        res=""
        pre=""
        cnt = 0
        for i in s:
            if i != pre:
                pre = i 
                cnt = 1
                res = res +i
            elif cnt >=2:
                continue
            else:
                res = res +i
                cnt += 1
        return res

print(Solution().makeFancyString( "aaabaaaa"))