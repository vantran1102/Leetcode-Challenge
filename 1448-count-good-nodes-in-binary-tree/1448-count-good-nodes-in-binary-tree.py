# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if root is None:
            return 0
        def dfs(node,max_node):
            nonlocal count
            if node is None:
                return
            if node.val >= max_node:
                count+=1    
            max_node = max(max_node, node.val)
            dfs(node.left,max_node)
            dfs(node.right,max_node)
        dfs(root, root.val)
        return count
