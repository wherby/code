class Solution(object):
    def fullBloomFlowers(self, flowers, persons):
        ls = []
        for s,e in flowers:
            ls.append((s,1,0))
            ls.append((e+1,-1,0))
        for i,p in enumerate(persons):
            ls.append((p,2,i))
        ans =[0]*len(persons)
        ls.sort()
        acc =0
        for x,diff,q in ls:
            if diff ==2:
                ans[q] = acc
            else:
                acc += diff
        return ans
    
re = Solution().fullBloomFlowers([[1,10],[3,3]],[3,3,2])
print(re)