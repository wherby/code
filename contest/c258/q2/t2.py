from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rls):
        dic1 =defaultdict(int)
        for r in rls:
            t = float(r[0]) / r[1]
            dic1[t]=dic1[t] +1
        cnt =0
        for k,v in dic1.items():
            if v>=2:
                cnt += v *(v-1) //2
        return cnt 

rectangles = [[1,7],[2,8],[8,8],[2,5],[2,8],[7,4]]
re = Solution().interchangeableRectangles(rectangles)
print(re)