# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        glowka = head
        actnode = head.next
        popval = head.val
        popnode = head

        while actnode is not None:

            if actnode.val != popval:
                popnode.next = actnode
                popnode = popnode.next
                popval = actnode.val
            actnode = actnode.next
        popnode.next = None
        return glowka