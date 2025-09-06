# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        curr=head
        bac=None
        while curr:
            nex=curr.next
            curr.next=bac
            bac=curr
            curr=nex
        return bac     
        