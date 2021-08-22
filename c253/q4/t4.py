import bisect
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles) :
        mono, res = [], []
        for a in obstacles:
            i = bisect.bisect(mono, a)
            res.append(i + 1)
            if i == len(mono):
                mono.append(0)
            mono[i] = a
            print(mono)
        return res


obstacles = [3,1,5,6,4,2]
print(Solution().longestObstacleCourseAtEachPosition(obstacles))