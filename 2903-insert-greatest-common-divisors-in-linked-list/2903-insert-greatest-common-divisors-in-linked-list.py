# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        li=[]
        while curr:
            li.append(curr.val)
            curr=curr.next
        win_size=2
        gcd_l=[]
        for i in range(len(li)-win_size+1):
            st=li[i:win_size+i]
            gcd=math.gcd(st[-2],st[-1])
            gcd_l.append(gcd)    
        fin=[]
        j=0
        for i in range(len(li)):
            fin.append(li[i])
            if i < len(gcd_l):
                fin.append(gcd_l[i])    
        dummy=ListNode()
        curr=dummy
        for i in fin:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next            

            
               
        