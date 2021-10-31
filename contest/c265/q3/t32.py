from collections import deque 
class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        queue =[[start,0]]
        dic={}
        dic[start] =1
        idx = 0
        def checkK(k):
            if k == goal:
                return True
            if   k  in dic:
                #print(k,dic)
                return False
            return True
        while queue:
            tq=[]
            for q in queue:
                k,idx = q
                if k == goal:
                    return idx
                if k >=0 and k <=1000: 
                    for n in nums:
                        t = n + k 
                        if checkK(t):
                            #print("aa")
                            tq.append([t,idx +1])
                            dic[t]=1
                        t = k -n
                        if checkK(t):
                            tq.append([t,idx +1])
                            dic[t]=1
                        t = k ^ n
                        if checkK(t):
                            tq.append([t,idx +1])
                            dic[t]=1
            queue =tq
            #print(len(queue))
        return -1

re =Solution().minimumOperations([-821076380,-675066150,-306144249,504919653,716238043,-124990086,-428244973,655635118,-685309701,-829855358,-383651019,-469183737,481606536,60542672,70931791,16572795,245816770,-764645310,149691790,350230253,306994852,189683672,999272836,811531837,-666576311,-612033029,649577485],495,-416969045)      
print(re)
re =Solution().minimumOperations([1,3],6,4)
print(re)