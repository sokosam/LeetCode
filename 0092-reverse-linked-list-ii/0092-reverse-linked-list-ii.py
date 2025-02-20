# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= 1
        amt = right - left

        def reverse(prev, node, left):
            if left == 0:
                next = node.next
                node.next = prev
                return node, next
            next = node.next
            node.next = prev 
            return reverse(node, next, left- 1)
        

        if left == 0:
            end = head
            ans, afterEnd = reverse(None, head, amt)
            end.next = afterEnd
            return ans
        else:
            curr = head
            prev = None
            while curr and left > 0:
                prev = curr
                curr = curr.next
                left -= 1
            start, afterEnd =reverse(prev, curr, amt)
            prev.next = start
            curr.next = afterEnd
        return head
                




        


            

