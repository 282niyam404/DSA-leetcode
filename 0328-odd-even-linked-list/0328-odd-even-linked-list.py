# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        x=[]
        while cur:
            x.append(cur.val)
            cur=cur.next
        even_idx=[x[i] for i in range(1,len(x),2)]
        odd_idx=[x[i] for i in range(0,len(x),2)]
        final=odd_idx+even_idx
        dummy=ListNode()
        curr=dummy
        for i in final:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next    


          
        