# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def pomoc(root, akt):

            if root.left == None and root.right == None:
                return 2 * akt + root.val
            elif root.left == None:
                return pomoc(root.right, 2 * akt + root.val)
            elif root.right == None:
                return pomoc(root.left, 2 * akt + root.val)
            else:

            
                return pomoc(root.left, 2 * akt + root.val) + pomoc(root.right, akt* 2 + root.val)

        if root:
            return pomoc(root, 0)


