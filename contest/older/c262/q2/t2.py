class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        m =len(grid)
        n = len(grid[0])
        cnt = n *m
        nums = []

        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        nums = sorted(nums)
        mid = 0
        if cnt %2 ==0:
            mid = [cnt//2,cnt //2-1]
        else:
            mid = [cnt //2]
        couldFind =True
        for i in range(cnt): 
            res = (nums[i]-nums[0])%x
            if res != 0:
                couldFind =False
        if couldFind == False:
            return -1
        cand =[]
        if len(mid) ==1:
            mdn = nums[mid[0]]
            for i in range(mdn -x , mdn +x):
                if (i-nums[0]) % x == 0:
                    cand.append(i)
        else:
            mdn2 = nums[mid[0]] +x
            mdn1 = nums[mid[1]] -x
            for i in range(mdn1,mdn2):
                if (i-nums[0]) %x ==0:
                    cand.append(i)
        def getNum(cand ,nums):
            res = 0
            for num in nums:
                res += abs(num - cand) //x
            return res
        ress = map(lambda x : getNum(x,nums),cand)
        return min(ress)

re =Solution().minOperations([[1,2],[3,4]], 2)
print(re)

        