# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        self.sum1=0
        if root is None and targetSum==0:
            return False
        
        self.flag=0

        def isLeafNode(node):
            return node.left is None and node.right is None

        def DFS(node):
            if node is None:
                return
            self.sum1+=node.val
            if isLeafNode(node) and self.sum1==targetSum:
                self.flag=1
            else:
                DFS(node.left)
                DFS(node.right)
            self.sum1-=node.val
             
        DFS(root)
        return self.flag==1


        