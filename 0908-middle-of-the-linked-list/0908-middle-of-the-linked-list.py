# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        curr=head
        while curr:
            li.append(curr)
            curr=curr.next
        mid=len(li)//2
        return li[mid]
        

        