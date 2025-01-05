# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Tuple, Optional

def getNext(str):
    le = len(str)
    next = [0]*le
    next[0] = 0
    i=0
    j =1
    while j !=le:
        if str[j]  == str[i]:
            i +=1 
            next[j] = i
            j +=1
        elif i !=0:
            i = next[i-1]
        else:
            next[j] =0
            j +=1
    return next

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        pat =[]
        cur = head
        while cur!=None:
            pat.append(cur.val)
            cur = cur.next

        patArr = getNext(pat)
        n =len(pat)
        #print(pat,patArr)

        def nextState(state,val):
            if pat[state] == val:
                state +=1
                return state
            else:
                if state != 0:
                    state =patArr[state -1]
                    return nextState(state,val)
                else:
                    return 0

        def dfs(node,state):
            if state == n:
                return True
            if node ==None:
                return False
            
            state = nextState(state,node.val)
            return dfs(node.left,state) or dfs(node.right,state)
        return dfs(root,0)