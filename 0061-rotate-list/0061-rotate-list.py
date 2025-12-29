# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        glowka = head
        
        n = 0
        while glowka is not None:
            n +=1
            glowka = glowka.next
        if n == 0:
            return head
        k = k%n
        if k == 0:
            return head
        act = head
        for _ in range(n-k-1):
            act = act.next
        
        nowaglowa = act.next
        act.next = None
        nowaact = nowaglowa
        for _ in range(k-1):
            nowaact = nowaact.next
        nowaact.next = head



        return nowaglowa
