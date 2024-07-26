# https://leetcode.cn/problems/remove-linked-list-elements/description/
from typing import List, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next  # 删除下一个节点
            else:
                cur = cur.next  # 继续向后遍历链表
        return dummy.next

#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/remove-linked-list-elements/solutions/2806456/tao-lu-ru-he-you-ya-di-shan-chu-lian-bia-ah8z/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。