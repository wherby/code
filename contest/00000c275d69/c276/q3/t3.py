
class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0]*(2*10**5+10)
        st = [0]

        for i in range(n):
            p,c = questions[i]
            if dp[i]> st[-1]:
                st.append(dp[i])
            dp[i+c+1] = max(dp[i+c+1],st[-1] +p)
        return max(dp)

re = Solution().mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])
print(re)