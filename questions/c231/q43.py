import sys
class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        n = len(nums)
        self.k = k
        self.frequent = [{} for i in range(k)]  # frequent[group][num] 表示第 group 组中 num 出现了几次
        changeToMode = 0                        # 所有组均换成众数需要几次修改
        for i in range(n):
            if nums[i] in self.frequent[i % k]:
                self.frequent[i % k][nums[i]] += 1
            else:
                self.frequent[i % k][nums[i]] = 1
            changeToMode += 1
        xorSum = 0
        mode = [0] * k          # 众数
        self.modeFreq = [0] * k # modeFreq[group] 表示第 group 组的众数出现了几次
        for group in range(k):
            for num, freq in self.frequent[group].items():
                if freq > self.modeFreq[group]:
                    mode[group] = num
                    self.modeFreq[group] = freq
            xorSum ^= mode[group]
            changeToMode -= self.modeFreq[group]    # 众数不用换
        self.res = sys.maxsize
        for group in range(k):
            # + modeFreq[group] 是因为要把众数也换掉
            # - frequent[group][xorSum ^ mode[group]] 是因为已经是 xorSum 的数字不用换
            self.res = min(self.res, changeToMode + self.modeFreq[group] - self.frequent[group].get(xorSum ^ mode[group], 0))
        self.dfs(0, 0, changeToMode)
        return self.res
    def dfs(self, group: int, xorSum: int, changed: int):
        '''
        :param group 遍历到第 group 组
        :param xorSum 前面 group-1 组的异或和
        :param changed 之前已经做了 changed 次修改
        '''
        if changed >= self.res:
            return
        if group == self.k - 1:
            # + modeFreq[group] 是因为要把众数也换掉
            # - frequent[group][xorSum] 是因为已经是 xorSum 的数字不用换
            self.res = min(self.res, changed + self.modeFreq[group] - self.frequent[group].get(xorSum, 0))
            return
        for num, f in self.frequent[group].items():
            self.dfs(group + 1, xorSum ^ num, changed + self.modeFreq[group] - f)

nums=[165,22,35,196,128,58,159,47,104,34,228,43,249,226,157,6,174,117,234,141,166,83,170,143,99,133,199,196,207,142,101,89,122,127,15,38,255,185,109,232,115,76,188,254,95,177,241,37,70,45,193,241,76,76]
k=21
re = Solution().minChanges(nums , k )
print(re)