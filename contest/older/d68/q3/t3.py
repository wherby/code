
class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        def verify(s,locked):
            #print(s,locked)
            mx,mn =0,0
            n = len(s)
            if n %2 ==1:
                return False
            for i in range(n):
                if locked[i]=="1":
                    if s[i]==")":
                        mx,mn = mx-1,mn-1
                        if mx <0:
                            return False
                    else:
                        mx,mn = mx+1,mn +1
                else:
                    if mx==0:
                        mx =1
                        mn +=1
                    else:
                        mx +=1
                        mn -=1
            
            if mx >=0 and mn <=0:
                return True
            else:
                return False
        n = len(s)
        rs = list(s)
        rs = rs[::-1]
        for i in range(n):
            if rs[i] =="(":
                rs[i] =")"
            else:
                rs[i] = "("

        if verify(s,locked) and verify(rs,locked[::-1]):
            return True
        else:
            return False


s="())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
locked="100011110110011011010111100111011101111110000101001101001111"
re = Solution().canBeValid(s, locked )
print(re)
