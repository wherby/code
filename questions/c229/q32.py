import functools
class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        m = len(multipliers)
        n = len(nums)
        @functools.lru_cache(1024) 
        def dfs(l,r):
            midx = l + n-1 -r
            if midx == m:
                return 0
            a = dfs(l+1,r)+ nums[l] *multipliers[midx]
            b = dfs(l,r-1)+nums[r] *multipliers[midx]
            return max(a,b)
        re = dfs(0,len(nums)-1)
        #print(re)
        return re

nums = [-854,-941,10,299,995,-346,294,-393,351,-76,210,897,-651,920,624,969,-629,985,-695,236,637,-901,-817,546,-69,192,-377,251,542,-316,-879,-764,-560,927,629,877,42,381,367,-549,602,139,-312,-281,105,690,-376,-705,-906,85,-608,639,752,770,-139,-601,341,61,969,276,176,-715,-545,471,-170,-126,596,-737,130]
multipliers =[83,315,-442,-714,461,920,-737,-93,-818,-760,558,-584,-358,-228,-220]
re =Solution().maximumScore(nums , multipliers )
print(re)