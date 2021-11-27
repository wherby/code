class Solution(object):
    def getCollisionTimes(self, cars):
        stack =[]
        n = len(cars)
        res = [-1] * n
        for i in range(n-1,-1,-1):
            curPos,curSpeed = cars[i]
            while stack:
                preIdex = stack[-1]
                if cars[preIdex][1] >= curSpeed:
                    stack.pop()
                else:
                    catTime = (cars[stack[-1]][0] - curPos) /(curSpeed- cars[stack[-1]][1])
                    if res[preIdex] ==-1 or res[preIdex] >= catTime:
                        res[i] =catTime
                        break
                    else:
                        stack.pop()
            stack.append(i)
        return res 


re = Solution().getCollisionTimes(cars = [[3,4],[5,4],[6,3],[9,1]])
print(re)