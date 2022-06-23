class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MX = len(pressedKeys ) +4
        dp =[0]*(MX)
        dp[0]=1
        dp1 =[0]*(MX)
        dp1[0]=1
        mod = 10**9+7
        for i in range(1,MX-1):
            for j in range(1,min(i+1,4)):
                dp[i] += dp[i-j]
            for j in range(1,min(i+1,5)):
                dp1[i] += dp1[i-j]
            dp[i] = dp[i]%mod
            dp1[i]= dp1[i]%mod
        cnt =1
        lastkey = ""
        lastI =0
        pressedKeys += "k"
        #print(dp1[:10],dp[:10])
        for a in pressedKeys:
            if a != lastkey :
                if lastkey != "9" and lastkey !="7":
                    cnt = cnt * dp[lastI] % mod  
                else:
                    cnt = cnt * dp1[lastI] % mod
                lastI =1
                lastkey = a   
            else:
                lastI +=1
        return cnt 
        

re = Solution().countTexts("222222222222222222222222222222222222")
print(re)
re = Solution().countTexts("22233")
print(re)
re = Solution().countTexts("55555555999977779555")
print(re)
re = Solution().countTexts("555555555555555555555557777777777777777777777777777777777777777777777888888888888888888888882222222222222222222222233333333333333333333333222222222222222222222226666666666666666666666655555555555555555555555666666666666666666666669999999999999999999999999999999999999999999999333333333333333333333337777777777777777777777722222222222222222222222888888888888888888888882222222222222222222222222222222222222222222222555555555555555555555555555555555555555555555544444444444444444444444333333333333333333333333333333333333333333333399999999999999999933333")
print(re)