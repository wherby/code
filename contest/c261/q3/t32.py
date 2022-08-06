import collections


class Solution(object):
    def stoneGameIX(self, stones):
        cnt =collections.Counter(a %3 for a in stones)
        if min(cnt[1],cnt[2]) ==0:
            return max(cnt[1],cnt[2]) >2 and cnt[0] %2 >0
        print("cc")
        print(cnt)
        return abs(cnt[1]-cnt[2]) >2 or cnt[0] %2 ==0

re = Solution().stoneGameIX([15,20,10,13,14,15,5,2,3])
print(re) #[2,1,1,2,2,2]
print(re ,False)
re = Solution().stoneGameIX( [19,2,17,20,7,17])
print(re) #[1,2,2,2,1,2]
print(re ,True)
re = Solution().stoneGameIX( [2,2,2])
print(re) #[1,2,2,2,1,2]


2,2,1,2,1,2,1
1,1,2,1,2,1