"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        s = deque()

        def helper(head):
            if not head:
                return 

            s.append(head)     
            helper(head.child)
            helper(head.next)
            head.next = None
            head.child = None

        helper(head)

        
        newHead = Node(1,None, None)
        curr = newHead
        while s:
            curr.next = s.popleft()
            curr.next.child = None
            curr.next.prev = curr
            curr = curr.next
        newHead.next.prev = None
        return newHead.next

            



