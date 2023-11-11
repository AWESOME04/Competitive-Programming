# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def ValidFunc(root, left, right):     
            if not root:
                return True
            if not(root.val < right and root.val > left):
                return False

            return (ValidFunc(root.left, left, root.val) and 
                    ValidFunc(root.right, root.val, right))

        return ValidFunc(root, float("-inf"), float("inf"))
