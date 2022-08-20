class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ls = [i for i in s ]
        cnt =0 
        def change(tls):
            ls = list(tls)
            ch = []
            for i in range(n-1):
                if ls[i] =="0" and ls[i+1] == "1":
                    ch.append(i)
            for i in ch:
                ls[i],ls[i+1]= ls[i+1],ls[i]
            return ls 
        while ls != change(ls):
            cnt +=1
            ls = change(ls)
        return cnt





re =Solution().secondsToRemoveOccurrences("0110101")
print(re)

# 11011