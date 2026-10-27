# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        
        while head:
            next = output.next
            output.next = ListNode(head.val)
            output.next.next = next
            head = head.next

        return output.next