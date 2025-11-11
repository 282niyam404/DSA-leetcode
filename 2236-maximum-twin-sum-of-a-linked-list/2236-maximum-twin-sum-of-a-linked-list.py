# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr=head
        li=[]
        while curr:
            li.append(curr.val)
            curr=curr.next
        left=0
        right=len(li)-1
        sum_l=[]
        while left<right:
            sum_l.append(li[left]+li[right])
            left=left+1
            right=right-1
        return max(sum_l)    


        