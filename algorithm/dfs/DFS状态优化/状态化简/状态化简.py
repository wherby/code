# https://leetcode.cn/problems/elevator-requests-iii/

from functools import cache
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        
        @cache
        def dfs(state,time,pos):
            if state == (1<<m) -1:
                return time
            res = 10**30
            for i in range(m):
                if (1<<i) & state ==0:
                    arr,flr = requests[i]
                    newT= max(time + abs(flr-pos) ,arr)
                    res = min(res, dfs(state | (1<<i),newT,flr))
            return res 
        res =  dfs(0,0,start)
        dfs.cache_clear()
        return res            

# 把 time 通过dfs 获取， 把pos 用last 代替
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        
        @cache
        def dfs(state, last):
            if state == 0:
                return 0
            arr, flr = requests[last]
            prev_state = state ^ (1 << last)
            
            if prev_state == 0:
                return max(abs(flr - start), arr)

            res = 10**30
            for prev in range(m):
                if prev_state & (1 << prev):
                    prev_time = dfs(prev_state, prev)
                    prev_flr = requests[prev][1]
                    cur_time = max(prev_time + abs(flr - prev_flr), arr)
                    res = min(res, cur_time) 
            return res
        full_state = (1 << m) - 1
        return min(dfs(full_state, last) for last in range(m))


re =Solution().elevatorRequests( n = 9, start = 0, requests = [[0,8],[6,5]])
print(re)