class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        sc= ord('a') + k
        ls = [ord(a) for a in s]
        n = len(s)
        idx = 0
        ls[n-1] +=1
        while 0<= idx< n:
            if ls[idx] == sc and idx ==0: #失败条件
                return ""
            elif ls[idx] == sc:  #反悔前一位
                ls[idx] =ord("a")
                idx -=1
                ls[idx] +=1
            elif (idx and ls[idx-1] == ls[idx] or( idx >1 and ls[idx-2]==ls[idx]) ):
                ls[idx]+=1
            else:
                idx +=1
        return "".join([chr(a) for a in ls])