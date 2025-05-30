# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        # using while:
        while root:
            if root.val ==val:
                return root
            if root.val<val:
                root=root.right
            else:
                root=root.left
        return None



        #DFS similar approach
        # if root is None or root.val==val:
        #     return root
        # if val<root.val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)
            
      

        