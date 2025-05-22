# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        
        #function that checks the left and right sub tree  of the given tree or the part of the tree
        def symm(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False

            return symm(root1.left, root2.right) and symm(root1.right, root2.left)

        return symm(root, root) 
        
        