# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp,l=head,0
        while temp != None:
            temp  = temp.next
            l=l+1
        
        cl=l-n
        if cl==0:
            return head.next

        node2=head

        i=1
        while i<cl:
            node2=node2.next
            i=i+1

        node2.next = node2.next.next
        return head

        
        
