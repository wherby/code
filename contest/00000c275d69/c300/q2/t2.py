# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict,deque
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        mx =[[-1]*n for _ in range(m)]
        dics =[[0,1],[1,0], [0,-1],[-1,0]]
        ls = deque([])
        cur = head
        while(cur):
            ls.append(cur.val)
            cur = cur.next
        x,y = 0,0 
        dic =0
        while ls:
            t = ls.popleft()
            mx[x][y] = t
            dx,dy = dics[dic][0],dics[dic][1]
            nx,ny = x+dx,y+dy
            if 0<=nx< m and 0<=ny<n and mx[nx][ny] == -1:
                x,y = nx,ny
            else:
                dic = (dic + 1)%4
                dx,dy = dics[dic][0],dics[dic][1]
                nx,ny = x+dx,y+dy
                x,y = nx,ny
        return mx


re =Solution()
print(re)