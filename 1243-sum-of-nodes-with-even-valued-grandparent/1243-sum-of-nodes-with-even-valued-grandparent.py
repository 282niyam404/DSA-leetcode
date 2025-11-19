# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        t=0
        if not root:
            return 0
        if (root.val%2)==0 :
            if root.left:
                if root.left.left:
                    t=t+root.left.left.val
                if root.left.right:
                    t=t+root.left.right.val
            if root.right:
                if root.right.left:
                    t=t+root.right.left.val
                if root.right.right:
                    t=t+root.right.right.val
        t += self.sumEvenGrandparent(root.left)
        t += self.sumEvenGrandparent(root.right)
        return t





        