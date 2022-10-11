# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp,length =head, 0
        while temp:
            temp = temp.next
            length+=1
        
        middle = length//2
        i=0
        
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        first = second = head
        
        while i<middle:
            second = second.next
            i+=1
            
        secHalf = reverse(second)
        
        while first and secHalf:
            if first.val != secHalf.val : return False
            first = first.next
            secHalf = secHalf.next
        return True
        
