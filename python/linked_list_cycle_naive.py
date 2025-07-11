# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# add seen items to set 
# if (curr.next).val is in set 
#     return true
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        #honest to god this quesiton would've taken me 5 minutes if i new sets could hold more than numbers
        # in a sense they dont and it really is doing an address comparison
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False