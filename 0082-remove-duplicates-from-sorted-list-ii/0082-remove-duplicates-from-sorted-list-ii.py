# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        li=[]
        while curr:
            li.append(curr.val)
            curr=curr.next
        coun=Counter(li)
        stk=[]
        for val,c in coun.items():
            if c==1:
                stk.append(val)   
        dummy=ListNode()
        cur=dummy
        for i in range(len(stk)):
            cur.next=ListNode(stk[i])
            cur=cur.next
        return dummy.next

        