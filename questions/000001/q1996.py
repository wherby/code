class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(reverse = True)
        cnt =0
        n = len(properties)
        #print(properties)
        lastMx =0
        nextMx = 0
        lastV =properties[0][0]
        for i in range(n):
            a= properties[i][1]
            b = properties[i][0]
            if b != lastV:
                lastV = b 
                lastMx = max(lastMx,nextMx)
                nextMx = max(nextMx,a)
            else:
                nextMx = max(nextMx,a)
            if a < lastMx:
                cnt +=1
            #print(cnt,lastMx,nextMx,a,b)
        return cnt

re = Solution().numberOfWeakCharacters([[10, 7], [10, 4], [7, 10], [7, 9], [7, 5], [6, 9]])
print(re)