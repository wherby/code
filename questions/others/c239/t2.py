

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n =len(s)
        lss =[]
        def dfs(i,ls):
            if i == n:
                lss.append(ls)
                return 
            for j in range(i+1,n+1):
                t = list(ls)
                if len(t)>0:
                    x1 = int(t[-1])
                    x2 = int(s[i:j])
                    if x1 != x2+1:
                        continue
                t.append(s[i:j])
                dfs(j,t)
        dfs(0,[])
        #print(lss)
        
        return len(lss)>1



re = Solution().splitString("050043")
print(re)