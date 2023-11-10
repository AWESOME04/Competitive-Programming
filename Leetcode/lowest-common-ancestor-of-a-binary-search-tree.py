# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        
        leftt = self.lowestCommonAncestor(root.left, p, q)
        rightt = self.lowestCommonAncestor(root.right, p, q)

        if leftt and rightt:
            return root
        return leftt or rightt
