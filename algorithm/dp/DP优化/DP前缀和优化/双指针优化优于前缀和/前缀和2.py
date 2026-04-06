from collections import defaultdict,deque

class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        mod = 10**9+7
        dic =defaultdict(list)
        for a in range(0,5001):
            t= sum([int(b) for b in str(a) ])
            dic[t].append(a)
        
        n = len(digitSum)

        dp = [0] * 5001
        for v in dic[digitSum[0]]:
            dp[v] = 1
            
        for i in range(1, n):
            prefix_sum = [0] * 5002
            for j in range(5001):
                prefix_sum[j+1] = (prefix_sum[j] + dp[j]) % mod
            
            new_dp = [0] * 5001
            for v in dic[digitSum[i]]:
                new_dp[v] = prefix_sum[v+1]
            dp = new_dp
            
        return sum(dp) % mod