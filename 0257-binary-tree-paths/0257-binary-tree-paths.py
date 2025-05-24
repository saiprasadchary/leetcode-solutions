# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):

        self.res=[]
        if root is None:
            return self.res
        def isLeafNode(node):
            return node.left is None and node.right is None

        def DFS(node, temp):
            if node is None:
                return
            temp.append(node.val)
            if isLeafNode(node):
                self.res.append(list(temp))
                
            else:
                DFS(node.left, temp)
                DFS(node.right, temp)
            temp.pop()
                
        DFS(root, [])
        ans=[]

        for i in self.res:
            an='->'.join(map(str, i))
            ans.append(an)
        
        return ans
        

            