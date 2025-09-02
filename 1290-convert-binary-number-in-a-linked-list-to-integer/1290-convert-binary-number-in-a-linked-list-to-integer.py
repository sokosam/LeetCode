# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        val = 0

        s = []
        while head:

            s.append(head.val)
            head=head.next
        
        i = 0
        while s:
            curr = s.pop()
            if curr == 1:
                mask = 1 << i
                val |= mask
            i +=1
        return val
