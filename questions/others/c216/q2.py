class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ls = [1]*n
        res = k -n
        idx = n-1
        while res > 0 and idx >=0:
            if res >=25:
                ls[idx] = 26
                res =res -25
                idx -=1
            else:
                ls[idx] =ls[idx] + res 
                res =0
                break
        re =[0]*n
        for i in range(n):
            t= ord('a') + ls[i] -1 
            re[i] = chr(t)
        return "".join(re)