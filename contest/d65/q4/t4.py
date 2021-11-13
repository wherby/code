
from sortedcontainers import  SortedList
class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()
        workers.sort()
        def chech_valid(ans):
            _tasks = SortedList(tasks[:ans])
            _works = workers[-ans:]
            remainPills = pills
            task_ids =0
            for work in _works:
                task = _tasks[task_ids]
                if task<=work:
                    task_ids +=1
                elif task<=work + strength and remainPills>0:
                    remainPills -=1
                    remove_task_ids = _tasks.bisect_right(work + strength)
                    _tasks.pop(remove_task_ids-1)
                else:
                    return False
            return True
        lo, hi = 0, min(len(tasks),len(workers))
        while lo < hi:
            mid = (lo + hi +1)//2
            if chech_valid(mid):
                lo = mid
            else:
                hi = mid -1
        return lo

re = Solution().maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10)
print(re)