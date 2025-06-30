# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #dummy head node that has value 0
        sol = ListNode()
        cur = sol
        #while list1 and list2 are not empty
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        #if list1 is not empty return end of the list
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return sol.next