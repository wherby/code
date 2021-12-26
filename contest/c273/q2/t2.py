class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        x,y = startPos
        m = len(s)
        res =[0]*m
        for i in range(m):
            x1,y1 = x,y
            isGood =True
            for j in range(i,m):
                t=s[j]
                if t=="U":
                    x1 -=1
                elif t =="D":
                    x1 +=1
                elif  t =="R":
                    y1 +=1
                elif t =="L":
                    y1 -=1
                if x1 <0 or x1>=n or y1 <0 or y1>=n:
                    isGood =False
                    break
            res[i] = j-i +isGood
        return res


re = Solution().executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU")
print(re)