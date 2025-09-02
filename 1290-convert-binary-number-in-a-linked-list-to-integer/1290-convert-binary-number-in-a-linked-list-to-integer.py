# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        

        val = 0
        count = 0
        while prev:
            
            if prev.val == 1:
                mask = 1 << count
                val |= mask
            count +=1
            prev=prev.next
        
        # i = 0
        # while s:
        #     curr = s.pop()
        #     if curr == 1:
        #         mask = 1 << i
        #         val |= mask
        #     i +=1
        return val
