from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        ins = [0] * (numCourses)
        for re in prerequisites:
            l = re[0]
            r = re[1]
            ins[l] +=1
        

