import heapq
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        ls =[]
        for i in range(1,n):
            if heights[i-1] < heights[i]:
                ls.append((heights[i]-heights[i-1],i))
        sm = 0 
        st=[]

        for k in ls:
            heapq.heappush(st,k)
            if len(st) > ladders:
                #print(st)
                x= heapq.heappop(st)
                sm += x[0]
                if sm> bricks:
                    return k[1]-1
        return n-1

re = Solution().furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1)
print(re)


            
