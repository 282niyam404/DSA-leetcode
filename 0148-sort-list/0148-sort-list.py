# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        val=[]
        curr=head
        while curr:
            val.append(curr.val)
            curr=curr.next
        val.sort()
        curr=head
        for v in val:
            curr.val=v
            curr=curr.next
        return head    

        