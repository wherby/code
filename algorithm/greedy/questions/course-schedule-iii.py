# https://leetcode.cn/problems/course-schedule-iii/description/

# 贪心， 按照完成时间排序，如果不符合则优先去除最大耗时任务

import heapq
class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        cnt= 0
        finish = 0
        courses.sort(key= lambda x :x[1])
        st =[]
        for dur, end in courses:
            finish += dur
            heapq.heappush(st, -dur)
            cnt +=1
            if finish > end:
                k = heapq.heappop(st)
                finish +=k
                cnt -=1
        return cnt
    
