# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfsPathSum(node, TotSum):
            if not node:
                return False

            TotSum += node.val

            if not node.left and not node.right:
                return TotSum == targetSum
            
            return (dfsPathSum(node.left, TotSum)
             or dfsPathSum(node.right, TotSum))

        return dfsPathSum(root, 0)
