'''
For 141 return true or false
For 142 we have to return the index where the loop is getting iterated


In this we are not using any HashSet 

We are using 
    Floyd's Tortoise & Hare (slow-fast head)
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

  #141
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow= head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
  
  #142
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (fast==slow):
                meet = fast
                while head!=meet:
                    head=head.next
                    meet=meet.next
                return head
        return None
