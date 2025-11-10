#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk=[]
        fin=[]
        curr=head
        while curr:
            stk.append(curr.val)
            if stk[-1] == 0:
                if len(stk) > 1:
                    fin.append(sum(stk[1:-1]))  
                stk = [0]  
            curr = curr.next
        dummy = ListNode()   
        curr = dummy         
        for val in fin:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next            

        