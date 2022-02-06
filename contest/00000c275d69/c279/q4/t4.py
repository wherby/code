
class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cnt =0
        for i,a in enumerate(s):
            if a =="1":
                cnt +=1
        leftGainls = [0]*n
        leftGain = 0
        leftGainMx =0
        for i, a in enumerate(s):
            if a == "0":
                leftGain -=1
            else:
                leftGain +=1
            leftGainMx = max(leftGainMx,leftGain)
            leftGainls[i] = max(0,leftGainMx)
        rightGainls = [0]*n
        rightGainMX =0
        rightGain = 0
        for i,a in enumerate(reversed(s)):
            if a == "0":
                rightGain -=1
            else:
                rightGain +=1
            rightGainMX = max(rightGainMX,rightGain)
            rightGainls[n-1-i] =max(0,rightGainMX)
        mn = 2*n
        #print(rightGainls,leftGainls,cnt)
        for i in range(n-1):
            mn = min(mn, 2*cnt - leftGainls[i]-rightGainls[i+1])
        mn = min(mn, 2*cnt - leftGainls[n-1])
        return mn

re = Solution().minimumTime("0")
print(re)
        

        