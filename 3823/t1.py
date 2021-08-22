#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3823/
class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lls = [nums[0]]*n
        rls = [nums[n-1]]*n
        for i in range(1,n):
            lls[i] = max(lls[i-1],nums[i])
            rls[n-1-i]=min(rls[n-i],nums[n-1-i])
        md = self.bfs(lls,rls, 0,n-1)
        #print(lls,rls)
        return md+1
        
    def bfs(self,lls,rls,left,right):
        #print(left,right)
        if left >= right:
            #return left
            if left == len(lls)-1:
                return 100000
            if lls[left] <= rls[left+1]:
                return left
            else:
                return 100000
            #return left
        mid = (left+right) //2
        if lls[mid] <= rls[mid+1]:
            right = mid
        else:
            #left = mid+1
            return min(self.bfs(lls,rls,left,mid-1),self.bfs(lls,rls,mid+1,right))
        return self.bfs(lls,rls,left,right)    

ls = [26,51,40,58,42,76,30,48,79,91]
a = Solution().partitionDisjoint(ls)
print(a)
a = Solution().partitionDisjoint([5,0,3,8,6])
print(a)
a = Solution().partitionDisjoint([17,57,60,41,36,85,68,44,25,31,84,34,51,25,47])
print(a)