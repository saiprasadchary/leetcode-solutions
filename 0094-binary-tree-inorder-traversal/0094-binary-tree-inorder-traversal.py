# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def inorderTraversal(self, root):
        stack=[]
        node = root
        res=[]
        
        while stack or node:
            if node is not None:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                res.append(node.val)
                node=node.right
        return res 



    # def inorderTraversal(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     res=[]
    #     def DFS(node):
    #         if node is None:
    #             return
    #         DFS(node.left)
    #         res.append(node.val)
    #         DFS(node.right)
    #     DFS(root)
    #     return res

    # def inorderTraversal(self, root):
    #     self.res=[]
    #     self.DFS(root)
    #     return self.res

    # def DFS(self, node):
    #     if node is None:
    #         return
    #     self.DFS(node.left)
    #     self.res.append(node.val)
    #     self.DFS(node.right)
    




        