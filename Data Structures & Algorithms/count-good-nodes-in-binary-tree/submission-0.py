# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        count = 0

        def dfs(node, max_val_seen):
            nonlocal count
            if node is None:
                return
            if node.val >= max_val_seen:
                count += 1

            m_v = max(max_val_seen, node.val)

            dfs(node.left, m_v)
            dfs(node.right, m_v)
        
        dfs(root,root.val)
        return count
