class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        n = len(s)
        i =0
        idx =0
        m = len(spaces)
        re =[0]*(6*10**5+2)
        idxx =0
        while i +idx < n+m:
            if idx<m and spaces[idx] ==i:
                re[idxx] = " "
                idx +=1
                idxx +=1
            else:
                re[idxx] = s[i]
                i +=1
                idxx +=1
        for i in range(6*10**5+2):
            if re[i] ==0:
                return "".join(re[:i]) 

re = Solution().addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6])
print(re)
