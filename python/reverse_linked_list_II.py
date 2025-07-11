# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Edge case
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head        
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        curr = prev.next
        for i in range(right - left):
            #pick one up, adjust pointers
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        return dummy.next
            