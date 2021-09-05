class Solution:
    
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        dic1 = {}
        for i in range(n):
            k = S[i]
            dic1[k]=i
        re = [-1]
        start =0
        index = 0
        while start< n:
            t = S[index]
            end = dic1[t]
            if end > start:
                start = end
            if index == start:
                re.append(start)
                start = index +1
            index = index +1
        reL = []
        m = len(re)
        for i in range(1,m):
            t = re[i] - re[i-1]
            reL.append(t)
        return reL


s = Solution()
s.partitionLabels("ababcbacadefegdehijhklij")
