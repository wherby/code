from typing import List, Tuple, Optional

from collections import defaultdict,deque
import math
INF  = math.inf

class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[INF,INF] for _ in range(n+1)]
        dp[0][0] = dp[0][1] = 0
        for i in range(n):
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + ((nums[i]+i) % 2))
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + ((1 + nums[i]+i) % 2))
        def getDiff(parity):
            changed = []
            noChanged = []
            for i in range(n):
                if (nums[i] + i) % 2 != parity:
                    changed.append(nums[i])
                else:
                    noChanged.append(nums[i])

            if not changed:
                return max(noChanged) - min(noChanged)

            maxNC = max(noChanged) if noChanged else -10**10
            minNC = min(noChanged) if noChanged else 10**10
            if len(set(changed)) == 1 and len(set(noChanged)) == 1 and changed[0] == noChanged[0]:
                return 1

            new_max = maxNC
            new_min = minNC

            for x in changed:
                if x >= maxNC:
                    new_max = max(new_max, x - 1)
                elif x <= minNC:
                    new_min = min(new_min, x + 1)
                else:

                    if x - 1 >= minNC and x - 1 <= maxNC:
           
                        pass
                    elif x + 1 >= minNC and x + 1 <= maxNC:
  
                        pass
                    else:

                        if x - 1 < minNC:
    
                            new_min = min(new_min, x - 1)
                        if x + 1 > maxNC:
                            new_max = max(new_max, x + 1)

            return new_max - new_min



            

        if dp[n][0] > dp[n][1]:
            parity = 1
            ret2 = getDiff(parity)
            return [dp[n][1], ret2]
        elif dp[n][0] < dp[n][1]:
            parity = 0
            ret2 = getDiff(parity)
            return [dp[n][0], ret2]
        else:
            parity = 0
            ret2 = getDiff(parity)
            parity = 1
            ret3 = getDiff(parity)
            return [dp[n][0], min(ret2,ret3)]







re =Solution().makeParityAlternating([7,7])
print(re)