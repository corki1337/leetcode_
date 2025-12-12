# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        liczba1 = ""
        liczba2 = ""


        while l1 != None:
            liczba1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            liczba2 += str(l2.val)
            l2 = l2.next

        strodtylu = str(int(liczba1[::-1]) + int(liczba2[::-1]))[::-1]

        glowa = ListNode(int(strodtylu[0]))
        act = glowa

        for i in range(1, len(strodtylu)):
            nowy = ListNode(int(strodtylu[i]))
            act.next = nowy
            act = nowy

        return glowa

        
        
