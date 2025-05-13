# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        #note: diameter need not include the root node of the tree
        if root == None:
            return 0
        self.maxi=0# this variable is attached in each and every iteration, and updated accordingly

        def maxdia(node):
            if(node==None):
                return 0
            lh=maxdia(node.left)
            rh=maxdia(node.right)
            
            self.maxi=max(self.maxi, lh+rh)

            return 1+max(lh,rh)
        
        maxdia(root)
        
        return self.maxi
       