class Solution(object):
    def reverseEvenLengthGroups(self, head):
        nodes =[]
        node = head
        while node:
            nodes.append(node.val)
            node= node.next

        n = len(nodes)
        i = 0
        j =1
        while i< n:
            if j %2 ==0 and i+j<=n or (n-i)%2==0 and n-i<j:
                nodes[i:i+j] =nodes[i:i+j][::-1]
            i+=j
            j+=1
        newHead = ListNode(0)
        node=newHead
        for x in nodes:
            node.next = ListNode(x)
            node =node.next
        return newHead.next