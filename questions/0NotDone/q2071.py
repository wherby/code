#https://leetcode.com/contest/biweekly-contest-65/problems/maximum-number-of-tasks-you-can-assign/
# use binary search for verification and greedy for find job

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
                    task_ids +=1   ## greedy remove least reuire task by index increase
                elif task<=work + strength and remainPills>0:
                    remainPills -=1
                    remove_task_ids = _tasks.bisect_right(work + strength)
                    _tasks.pop(remove_task_ids-1)   ## greedy remove  task to be handle
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