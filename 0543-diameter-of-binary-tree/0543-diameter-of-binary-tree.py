# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.result = 0

        def height(curr):
            if not curr:
                return 0
            left = height(curr.left)
            right = height(curr.right)
            self.result = max(self.result, left+right) #result = max(left + right)
            return 1 + max(left,right) 

        height(root)
        return self.result

        