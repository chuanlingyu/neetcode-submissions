# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        head = output
        
        while list1 or list2:
            if list1 and list2:

                if list1.val < list2.val:
                    output.next = list1
                    list1 = list1.next
                else:
                    output.next = list2
                    list2 = list2.next
            
            elif list1:
                output.next = list1
                break
            
            else:
                output.next = list2
                break

            output = output.next

        return head.next