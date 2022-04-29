import heapq
class Solution(object):
    def buildBridge(self, num, wood):
        """
        :type num: int
        :type wood: List[List[int]]
        :rtype: int
        """
        l,r =0,0
        ans = 0
        left,right =[],[]
        n = len(wood)
        left.append(-wood[0][0])
        right.append(wood[0][0])
        #print(left,right)
        for i in range(1,n):
            print(ans,l,r)
            r += wood[i-1][1]-wood[i-1][0]
            l -= wood[i][1] - wood[i][0]
            ans += max(0,max(l-left[0]-wood[i][0],wood[i][0]-r - right[0]))
            print(sorted(left),sorted(right),wood[i],l,r,l-left[0]-wood[i][0],wood[i][0]-r - right[0])
            if wood[i][0]< l-left[0]:
                heapq.heappush(right,l-r-heapq.heappop(left))
                heapq.heappush(left,l- wood[i][0])
                heapq.heappush(left,l- wood[i][0])
            elif wood[i][0]> r + right[0]:
                heapq.heappush(left, l-r- heapq.heappop(right))
                heapq.heappush(right,wood[i][0] - r)
                heapq.heappush(right,wood[i][0] - r)
            else:
                heapq.heappush(left,l -wood[i][0])
                heapq.heappush(right,wood[i][0] - r)
            print(sorted(left),sorted(right))
        return ans 
    
re =Solution().buildBridge( num = 10, wood = [[1,2],[4,7],[8,9]])
print(re)
                   