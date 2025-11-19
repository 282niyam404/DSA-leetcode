# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        li=[]
        def preorder(node,li):
            if not node:
                return None
            if node.left and not node.left.left and not node.left.right:
                li.append(node.left.val)
            preorder(node.left,li)
            preorder(node.right,li)
            return li
        preorder(root,li)
        x=sum(li)    
        return x
                   
        