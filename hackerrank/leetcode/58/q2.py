#https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        re =[None]*k
        index =0
        pt = root
        n =0
        nre = [0]*k
        while pt != None:
        	n = n+1
        	pt = pt.next
        for i in range(k):
        	nre[i] = (n+k-i -1)/k
        pt=root
        nreIndex =0
        while pt != None:
        	t1 = nre[nreIndex]
        	for i in range(t1):
        		pv = pt.val
        		if re[nreIndex] == None:
        			re[nreIndex] = ListNode(pv)
        		else:
        			ppv = re[nreIndex]
        			while ppv.next !=None:
        				ppv = ppv.next
        			ppv.next = ListNode(pv)
        		pt = pt.next
        	nreIndex = nreIndex +1
        return re