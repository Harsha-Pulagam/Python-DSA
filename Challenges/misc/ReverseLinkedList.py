# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev
"""
Explanation:
input : 1->2->3->4

while curr: (not null)

first iteration:
prev = None , curr = head (at value 1)
while curr: (not null)
    nextNode = curr.next (assigning position of 2 to nextnode)
        curr.next = prev  (here prev is None,end of the list is none so assigning it )
        prev = curr (position of 1 is named as prev)
        curr = nextNode (moving curr to position 2 i.e nextnode)
        
        None<-1   2->3->4
        
Second iteration:
prev = at val 1 , curr = head (at value 2)
while curr: (not null)
    nextNode = curr.next (assigning position of 3 to nextnode)
        curr.next = prev  (here prev is at 1, so assigning it )
        prev = curr (position of 2 is named as prev)
        curr = nextNode (moving curr to position 3 i.e nextnode)
                
        None<-1<-2   3->4
        
        and so on..
"""