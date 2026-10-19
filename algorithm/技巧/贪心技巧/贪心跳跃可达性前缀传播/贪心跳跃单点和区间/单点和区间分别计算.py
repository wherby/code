# https://leetcode.cn/problems/minimum-interval-selection-to-cover-target-intervals/description/
from typing import List, Tuple, Optional
class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        if not targetIntervals:
            return 0
        
        targetIntervals.sort(key=lambda x: x[0])
        merged_targets = []
        for interval in targetIntervals:
            if not merged_targets or merged_targets[-1][1] < interval[0]:
                merged_targets.append(list(interval))
            else:
                merged_targets[-1][1] = max(merged_targets[-1][1], interval[1])

        availableIntervals.sort(key=lambda x: x[0])
        
        count = 0
        i = 0
        n = len(availableIntervals)
        covered_upto = -1
        
        for t_start, t_end in merged_targets:
            if covered_upto >= t_end:
                continue
                
            covered_upto = max(covered_upto, t_start)
            

            if t_start == t_end:
                max_reach = covered_upto - 1
                found = False
                while i < n and availableIntervals[i][0] <= covered_upto:
                    if availableIntervals[i][1] >= t_start:
                        if availableIntervals[i][1] > max_reach:
                            max_reach = availableIntervals[i][1]
                            found = True
                    i += 1
                if not found or max_reach < t_end:
                    return -1
                covered_upto = max_reach
                count += 1
                continue
                

            while covered_upto < t_end:
                max_reach = covered_upto
                found = False
                
                while i < n and availableIntervals[i][0] <= covered_upto:
                    if availableIntervals[i][1] > max_reach:
                        max_reach = availableIntervals[i][1]
                        found = True
                    i += 1
                    
                if not found or max_reach == covered_upto:
                    return -1
                    
                covered_upto = max_reach
                count += 1
                
                if covered_upto >= t_end:
                    break
                    
            if covered_upto < t_end:
                return -1
                
        return count