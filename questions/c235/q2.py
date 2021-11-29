from collections import defaultdict
class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ls =[0]*(k+1)
        rec =defaultdict(list)
        for a,t in logs:
            rec[a].append(t)
        for k,v in rec.items():
            ls[len(set(v))] +=1
        
        return ls[1:]

re = Solution().findingUsersActiveMinutes(logs =[[305589003,4136],[305589004,4139],[305589004,4141],[305589004,4137],[305589001,4139],[305589001,4139]], k = 6)
print(re)