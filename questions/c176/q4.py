import heapq
class Solution:
    def isPossible(self, target: list[int]) -> bool:
        n = len(target)
        sm = sum(target)
        cnt = 0
        st =[]
        for a in target:
            if a ==1:
                cnt +=1
            else:
                heapq.heappush(st,-a)
        while st:
            k = heapq.heappop(st)
            if k ==-1:
                cnt +=1
                continue
            elif k >-1:
                break
            other = sm +k
            if other ==0:
                break
            kfa = sm //(other*2)
            if kfa >1:
                ok = sm -other*2*(kfa-1)
            else:
                ok = sm-other *2
            #print(ok)
            if ok >1:
                heapq.heappush(st,-ok)
            elif ok ==1:
                cnt  +=1
            else:
                return False
            sm = other +ok
        if cnt ==n:
            return True
        else:
            return False
re = Solution().isPossible([62305,12,1,1321,1,31153,45,4577,16721,23,1,1])
print(re)
        
            