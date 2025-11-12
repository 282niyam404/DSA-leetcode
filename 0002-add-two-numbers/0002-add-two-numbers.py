# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str=""
        l2_str=""
        curr1=l1
        curr2=l2
        while curr1:
            l1_str=l1_str+str(curr1.val)
            curr1=curr1.next
        while curr2:
            l2_str=l2_str+str(curr2.val)
            curr2=curr2.next
        x=str(int(l1_str[::-1])+int(l2_str[::-1]))[::-1]   
        l=[int(x[i]) for i in range(len(x))]
        dummy=ListNode()
        curr=dummy
        for i in range(len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        return dummy.next    
        


        

        