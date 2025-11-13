# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        li=[]
        while curr:
            li.append(curr.val)
            curr=curr.next
        mid=len(li)//2
        li.pop(mid)
        dummy=ListNode()
        cur=dummy
        for i in range(len(li)):
            cur.next=ListNode(li[i])
            cur=cur.next
        return dummy.next        
        