# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less = None
        ge = None
        lessStart = None
        geStart = None

        curr = head

        while curr:
            if curr.val < x:
                if less:
                    less.next = curr
                    less = less.next
                else:
                    lessStart = curr
                    less = curr
            else:
                if ge:
                    ge.next = curr
                    ge = ge.next
                else:
                    geStart = curr
                    ge = curr
            curr = curr.next
        if ge:
            ge.next = None
        
        if less:
            less.next = geStart
        else:
            return geStart
        return lessStart
