# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk=[]
        curr=head
        while curr:
            while stk and curr.val>stk[-1]:
                
                stk.pop()    
            stk.append(curr.val)
            curr=curr.next
        d=ListNode()
        cur=d
        for n in stk:
            cur.next=ListNode(n)
            cur=cur.next
        return d.next        