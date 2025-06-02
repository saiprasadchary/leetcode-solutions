# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node=root
        if root is None:
            return TreeNode(val)

        while node:
            if node.val <= val:
                if node.right is None:
                    node.right=TreeNode(val)
                    break
                else:
                    node=node.right
                    
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node=node.left        
        return root