# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk=[]
        def preord(node,stk):
            if not node:
                return None
            stk.append(node.val)
            preord(node.left,stk)
            preord(node.right,stk)
            return stk 
        preord(root,stk)
        final_l_sort=sorted(stk)
        return final_l_sort[k-1]       
                

            

        