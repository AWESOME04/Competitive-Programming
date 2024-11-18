# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []
        while queue:
            qLen = len(queue)
            level = []
            for i in range(qLen):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level = list(reversed(level)) if len(res) % 2 else level
            res.append(level)

        return res
