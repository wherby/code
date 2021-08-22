from queue import PriorityQueue
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        index = [i for i in range(len(times))]
        indexWithTime = list(zip(times,index))
        timeQ = PriorityQueue()
        avQ = PriorityQueue()
        for timeIndex in indexWithTime:
            timeQ.put([timeIndex[0][0]+0.1,timeIndex[1],0])
            timeQ.put([timeIndex[0][1],timeIndex[1],1])
        res =[]
        while not timeQ.empty():
            res.append(timeQ.get())
        next =0
        dic1={}
        for item in res:
            if item[2] ==0:
                if item[1] == targetFriend:
                    if avQ.empty():
                        return next
                    else:
                        return avQ.get()
                else:
                    if avQ.empty():
                        dic1[item[1]] = next
                        next =next +1
                    else:
                        t = avQ.get()
                        dic1[item[1]] = t
            else:
                avQ.put(dic1[item[1]])


        
times = [[1,4],[2,3],[4,6]]
a =Solution().smallestChair(times,1)
print(a)
times = [[3,10],[1,5],[2,6]]
a =Solution().smallestChair(times,0)
print(a)
times = [[18,19],[10,11],[21,22],[5,6],[2,3],[6,7],[43,44],[48,49],[53,54],[12,13],[20,21],[34,35],[17,18],[1,2],[35,36],[16,17],[9,10],[14,15],[25,26],[37,38],[30,31],[50,51],[22,23],[3,4],[27,28],[29,30],[33,34],[39,40],[49,50],[15,16],[4,5],[46,47],[51,52],[32,33],[11,12],[28,29],[47,48],[36,37],[40,41],[42,43],[52,53],[41,42],[31,32],[23,24],[8,9],[19,20],[24,25],[26,27],[45,46],[44,45],[7,8],[13,14],[38,39]]
a =Solution().smallestChair(times,8)
print(a)