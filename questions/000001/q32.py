# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def merge2List(self,list1,list2):
        head = ListNode()
        pre = head
        while (list1 and list2):
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
        pre.next = list1 if list1 else list2
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) ==0:
            return None
        
        if len(lists) ==1:
            return lists[0]
        mid = len(lists) //2
        return self.merge2List(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))

# re =Solution().mergeKLists([[1,4,5],[1,3,4],[2,6]])
# print(re)