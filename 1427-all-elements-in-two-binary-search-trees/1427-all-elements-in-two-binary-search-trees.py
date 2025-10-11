# Definition for a binary tree node.
# 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        l=[]
        
        def in_ord(x,l):
            if not x:
                return 
            in_ord(x.left,l)
            l.append(x.val)
            in_ord(x.right,l)
            
        in_ord(root1,l)
        in_ord(root2,l)
        x=sorted(l)
        return x










        