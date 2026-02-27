# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            glowka = ListNode(list1.val)
            list1 = list1.next
        else: 
            glowka = ListNode(list2.val)
            list2 = list2.next
            
        

        
        
        act = glowka

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                
                act.next =  ListNode(list1.val)
                act = act.next
                list1 = list1.next
                

            else:
                
                act.next = ListNode(list2.val)
                
                act = act.next
                list2 = list2.next
                
        if list1 is None and list2 is not None:
            act.next = list2
        elif list2 is None and list1 is not None:
            act.next = list1


        return glowka
            


        