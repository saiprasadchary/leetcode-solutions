# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def helper(node):
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            right_child=node.right
            last_child=findLastChild(node.left)
            last_child.right=right_child
            return node.left

        def findLastChild(node):
            while node.right:
                node=node.right
            return node

        if root is None:
            return None

        if root.val==key:
            return helper(root)

        node=root
        while node:
            if node.val>key:
                if node.left and node.left.val==key:
                    node.left=helper(node.left)
                    break
                else:
                    node=node.left
            else:
                if node.right and node.right.val==key:
                    node.right=helper(node.right)
                    break
                else:
                    node=node.right
        return root

        