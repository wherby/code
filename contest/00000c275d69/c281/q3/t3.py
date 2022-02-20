class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        ls = [0]*26
        for a in s:
            k = ord(a) -ord('a')
            ls[k]+=1
        lkey = -1
        n = len(s)
        res =[]
        for i in range(n):
            for j in range(25,-1,-1):
                #print(i,j,lkey,res)
                if ls[j] >0:
                    if j != lkey:
                        lkey=j
                        t = min(ls[j],repeatLimit)
                        ls[j] -=t
                        t1 = chr(ord('a') +j)
                        #print("aaaa",t1,j)
                        res.append(t1 *t)
                        #print(ls)
                        break
                    else:
                        isF = False
                        for k in range(j-1,-1,-1):
                            if ls[k]>0:
                                res.append(chr(ord('a') +k))
                                lkey =k
                                ls[k] -=1
                                isF = True
                                break
                        if(isF == False):
                            #print(res,isF,j)
                            return "".join(res)
                        break
            #print(ls)
            
        #print(res)
        return "".join(res)

re = Solution().repeatLimitedString(s = "aababab", repeatLimit = 2)
print(re)

        