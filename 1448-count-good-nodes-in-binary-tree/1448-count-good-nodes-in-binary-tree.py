# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Option 1:
        # count = 0
        # if root is None:
        #     return 0
        # def dfs(node,max_node):
        #     nonlocal count
        #     if node is None:
        #         return
        #     if node.val >= max_node:
        #         count+=1    
        #     max_node = max(max_node, node.val)
        #     dfs(node.left,max_node)
        #     dfs(node.right,max_node)
        # dfs(root, root.val)
        # return count
        #-----------------------------#
        #Option 2:
        def dfs(root,max_node,count):
            if root is None:
                return 0
            if root.val >= max_node:
                count+=1
                max_node = root.val
            if root.left is not None:
                count += dfs(root.left,max_node,0)
            if root.right is not None:
                count += dfs(root.right,max_node,0)
            return count
        max_node = float("-inf")
        count = 0
        return dfs(root,max_node,count)