# https://leetcode.cn/problems/super-egg-drop/?envType=daily-question&envId=2024-10-14
from functools import cache
from itertools import count
# dfs(i,j) 表示用i次扔和j个鸡蛋能测试多少层楼

@cache
def dfs(i,j):
    if i ==0 or j ==0:
        return 0 
    return dfs(i-1,j) + dfs(i-1,j-1)+1
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        for i in count(1):
            if dfs(i,k)>=n:
                return i 

re = Solution().superEggDrop(3,14)
print(re)