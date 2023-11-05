class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        sa = zip(ages,scores)
        sa =sorted(sa)
        n = len(sa)
        dp =[0]*n
        dp[0] = sa[0][1]
        for i in range(1,n):
            dp[i] = sa[i][1]
            for j in range(i):
                # if sa[i][0]==sa[j][0] and sa[i][1] >=sa[j][1]:
                #     dp[i] = max(dp[i],dp[j] + sa[i][1])
                if  sa[i][1] >=sa[j][1]:
                    dp[i] =max(dp[i], dp[j] + sa[i][1])
        #print(dp,sa,sa[0][1])
        return max(dp)


re =Solution().bestTeamScore(scores = [1,1,1,1,1,1,1,1,1,1], ages = [811,364,124,873,790,656,581,446,885,134])