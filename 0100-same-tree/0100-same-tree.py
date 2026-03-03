# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val == q.val:
            if (p.left is None and q.left is None) and (p.right is None and q.right is None):
                return True
            elif (p.left is not None and q.left is not None) and (p.right is None and q.right is None):
                return self.isSameTree(p.left, q.left)
            elif (p.left is None and q.left is None) and (p.right is not None and q.right is not None):
                return self.isSameTree(p.right, q.right)
            elif (p.left is not None and q.left is not None) and (p.right is not None and q.right is not None):
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
            else:
                return False
            
        else:
            return False