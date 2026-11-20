# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = []
        already_itteration = -1

        def bfs(node, level):
            if len(ret) == level:
                ret.append([])

            ret[level].append(node.val)

            if node.left != None:
                bfs(node.left, level +1)
            if node.right != None:
                bfs(node.right, level +1)
        bfs(root,0)
        return ret