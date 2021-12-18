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
        

courses =[[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
re = Solution().scheduleCourse(courses)
print(re)
