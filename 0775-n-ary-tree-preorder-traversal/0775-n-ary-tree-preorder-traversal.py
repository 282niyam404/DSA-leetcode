"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        li=[]
        if not root:
            return None
        li.append(root.val)
        for child in root.children or []:
            li.extend(self.preorder(child)) 
        return li

        