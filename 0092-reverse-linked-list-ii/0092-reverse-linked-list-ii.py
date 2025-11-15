# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li=[]
        curr=head
        while curr:
            li.append(curr.val)
            curr=curr.next
        while left<right:
            li[left-1],li[right-1]=li[right-1],li[left-1]
            left=left+1
            right=right-1
        dummy=ListNode
        cur=dummy
        for i in range(len(li)):
            cur.next=ListNode(li[i])
            cur=cur.next
        return dummy.next    


        