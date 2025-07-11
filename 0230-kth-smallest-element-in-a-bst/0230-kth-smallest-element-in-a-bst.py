# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        if root is None:
            return None
        self.res=0
        self.cnt=0

        #DFS approach(Pre-order)
        def DFS(node, k):
            if node is None:
                return

            DFS(node.left, k)
            self.cnt+=1

            if self.cnt==k:
                self.res= node.val

            DFS(node.right, k)

        DFS(root, k)
        #print(self.res, self.cnt)

        return self.res
        
    
       
        