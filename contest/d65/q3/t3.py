from bisect import bisect_right
class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        n =len(items)
        items.sort()
        pre = [0]*(n+1)
        price= [x[0] for x in items]
        for i in range(n):
            pre[i+1] = max(pre[i],items[i][1])
        res = []
        #print(items, pre)
        for q in queries:
            idx = min(bisect_right(price,q),n)
            #print(q,idx)
            res.append(pre[idx])
        return res


re = Solution().maximumBeauty(items = [[10,1000]], queries = [5]) 
print(re)