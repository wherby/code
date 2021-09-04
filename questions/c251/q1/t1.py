class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = []
        for i in s:
            t = ord(i)-ord('a')+1
            if t >=10:
                res.append(t%10)
                res.append(t//10)
            else:
                res.append(t)
        re1 =0
        for j in range(k):
            re1 = sum(res)
            re =re1
            tp=[]
            while re >0:
                tp.append(re%10)
                re = re //10
            res = tp 
        return re1

a=Solution().getLucky("leetcode",2)
print(a)