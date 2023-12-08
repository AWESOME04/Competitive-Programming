# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
            queue = deque([root])
            avgs = []

            while queue:
                curr_level = len(queue)
                tot = 0

                for i in range(curr_level):
                    curr = queue.popleft()
                    tot += curr.val

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                avgs.append(tot/curr_level)
            return avgs
        
