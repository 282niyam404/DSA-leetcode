# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        act=""
        cur=head
        while cur:
            act+=str(cur.val)
            cur=cur.next
        carry = 0
        res = []
        for d in reversed(act):
            s = int(d) * 2 + carry
            res.append(str(s % 10))
            carry = s // 10
        if carry:
            res.append(str(carry))
        dob_act = "".join(reversed(res))
        dumy=ListNode()
        curr=dumy
        for i in dob_act:
            curr.next=ListNode(int(i))
            curr=curr.next
        return dumy.next         

        