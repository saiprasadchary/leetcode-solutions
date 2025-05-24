# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        self.res=[]
        self.sum1=0
        if root is None and targetSum==0:
            return self.res
        
        def isLeafNode(node):
            return node.left is None and node.right is None

        def DFS(node, temp):
            if node is None:
                return
            temp.append(node.val)
            self.sum1+=node.val

            if self.sum1==targetSum and isLeafNode(node):
                self.res.append(list(temp))   
            else:
                DFS(node.left, temp)
                DFS(node.right, temp)

            self.sum1-=node.val
            temp.pop()

        DFS(root, [])
        return self.res
        