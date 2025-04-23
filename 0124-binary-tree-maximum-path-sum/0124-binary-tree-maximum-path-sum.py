# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0
        self.maxPathSum = float("-inf")
        
        def maxPath(node):
            if(node is None):
                return 0

            # It explores the depth of left and right-> leafs
            leftSum=maxPath(node.left)
            rightSum=maxPath(node.right)

            leftSum=max(0, leftSum)
            rightSum=max(0, rightSum)

            self.maxPathSum=max(self.maxPathSum, leftSum+rightSum+node.val)


            # the above leftSum and rightSum logic is defined here
            return node.val+max(leftSum, rightSum)
            
        maxPath(root)
        return self.maxPathSum
        