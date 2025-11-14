# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        #check if bot root is None
        if not q and not p:
            return True
        
        #check if one of the root is None:
        if not q or not p:
            return False
        
        #check roots values
        if q.val != p.val:
            return False
        #return result by using recursive function. check if both side of trees is equal
        return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)

        