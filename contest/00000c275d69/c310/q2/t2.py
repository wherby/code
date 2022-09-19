class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n= len(s)
        ls = [0]*26
        cnt =1
        for i in range(n):
            k = ord(s[i]) - ord('a')
            #print(ls[k],i, i != n-1)
            if ls[k] ==1:
                for j in range(26):
                    ls[j] =0
                ls[k] =1
                cnt +=1
            else:
                ls[k] =1
            #print(ls,cnt,n,ls[k],k)
        return cnt



re =Solution().partitionString("abacaba")
print(re)