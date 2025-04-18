# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        def dfs(node):
            if(node==None):
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

# another approach

    # def preorderTraversal(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     # Initialize the result list on the instance
    #     self.res = []
    #     # Kick off the real recursion
    #     self._preorder(root)
    #     return self.res
    
    # def _preorder(self, node):
    #     # Base case
    #     if node is None:
    #         return
    #     # Visit
    #     self.res.append(node.val)
    #     # Recurse left, then right
    #     self._preorder(node.left)


        