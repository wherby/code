class Solution:
    def largestPalindromic(self, num: str) -> str:
        ls =[0]*10
        for a in num:
            ls[int(a)] +=1
        oddN = ""
        ret =""
        for i in range(9,-1,-1):
            if ls[i] %2 ==1 and oddN=="":
                oddN = str(i)
            if i ==0 and ret =="":continue
            ret += str(i)*(ls[i]//2)
        half = ret
        if oddN !="":
            ret += oddN
        ret += half[::-1]
        if ret =="":
            return "0"
        return ret





re =Solution().largestPalindromic(num = "444947137")
print(re)