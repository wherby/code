# Linked list

## reverse link list

revert link list it's better to have a dummy node to print to head
https://leetcode.com/problems/reverse-linked-list-ii/discuss/1575832/Python-3

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_left, curr = dummy, head
                
        # 1. find the left pointer by moving (left - 1) times
        for _ in range(left - 1):
            prev_left, curr = curr, curr.next
        
        # 2. reverse (right - left + 1) times
        prev_right = None
        for _ in range(right - left + 1):
            curr.next, curr, prev_right = prev_right, curr.next, curr
        
        # 3. connect
        prev_left.next.next, prev_left.next = curr, prev_right
        
        return dummy.next