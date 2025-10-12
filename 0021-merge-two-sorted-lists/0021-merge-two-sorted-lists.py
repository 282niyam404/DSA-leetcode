# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        curr1=list1
        curr2=list2
        while curr1:
            l1.append(curr1.val)
            curr1=curr1.next
        while curr2:
            l2.append(curr2.val)
            curr2=curr2.next
        final_l=sorted(l1+l2)
        dummy=ListNode()
        cur=dummy
        for i in final_l:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next 
        