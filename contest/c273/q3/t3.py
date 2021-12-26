from collections import defaultdict
from bisect import bisect_right
class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dic =defaultdict(list)
        for i,a in enumerate(arr):
            dic[a].append(i)
        dic2 ={}
        n = len(arr)
        res = [0]*n
        for i in range(n):
            t = arr[i]
            if t not in dic2:
                tls = dic[t]
                m = len(tls)
                pre = [0]*(m+1)
                for j in range(m):
                    pre[j+1] = pre[j] +tls[j]
                dic2[t] = pre
            pre = dic2[t]
            idxls = dic[t]
            m = len(idxls)
            kidx = bisect_right(dic[t],i)
            #print(pre,idxls,kidx,)
            gain = (kidx-1)* i -pre[kidx-1] + pre[m] - pre[kidx] - (m-kidx)*i
            #print((kidx-1)* i,pre[kidx-1],pre[m] - pre[kidx] - (m-kidx)*i)
            res[i] = gain
        return res

re = Solution().getDistances(arr = [2,1,3,1,2,3,3])
print(re)
