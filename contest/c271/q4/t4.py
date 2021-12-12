from bisect import bisect_right,bisect_left
class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        posible=[]
        for i in range(k+1):
            maxRight =startPos + i
            maxLeft = min(startPos, startPos- (k-i*2))
            posible.append([maxLeft,maxRight])
        for i in range(k+1):
            maxLeft = max(0,startPos-i)
            maxRight = max(startPos,startPos +(k-i*2))
            posible.append([maxLeft,maxRight])
        n = len(fruits)
        preFix = [0]*(n+1)
        positionLs= [0]*(n)
        for i in range(n):
            preFix[i+1] = preFix[i] + fruits[i][1]
            positionLs[i] = fruits[i][0]
        mx =0
        #print(posible)
        for left,right in posible:
            leftIdx = bisect_left(positionLs,left)
            rightIdx =bisect_right(positionLs,right)
            mx = max(mx, preFix[rightIdx]-preFix[leftIdx])
        return mx


re= Solution().maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4)
print(re)

