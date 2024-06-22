# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        def helper(root, level):
            if root:
                if len(res) == level:
                    res.append(root.val)
                
                helper(root.right, level + 1)
                helper(root.left, level + 1)
            return
            
        res = []
        helper(root, 0)
        return res

# TC: O(N)
# SC: O(N)
