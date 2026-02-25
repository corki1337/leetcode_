# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def pomoc(root, akt):

            if root.left == None and root.right == None:
                return 10 * akt + root.val
            elif root.right == None:
                return pomoc(root.left, 10 * akt + root.val) 
            elif root.left == None:
                return pomoc(root.right, 10 * akt + root.val)
            else:
                return pomoc(root.right, 10 * akt + root.val) + pomoc(root.left, 10 * akt + root.val)
        
        if root:
            return pomoc(root, 0)