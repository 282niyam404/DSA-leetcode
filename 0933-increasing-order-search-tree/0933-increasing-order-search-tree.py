# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #first inorder treversal
        def inorder(root):
            if not root:
                return None
            yield from inorder(root.left)
            yield root
            yield from inorder(root.right)
        r=TreeNode(-1)
        c=r
        for n in inorder(root):
            n.left=None
            c.right=n
            c=n
        return r.right    


        