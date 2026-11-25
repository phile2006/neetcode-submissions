# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0

        seen = []

        def dfs(node):
            if node is None:
                return
            seen.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        seen.sort(reverse=True)
        return seen[-k]