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
        self.res=[]

        #DFS approach(Pre-order)
        def DFS(node, k):
            if node is None:
                return

            DFS(node.left, k)
            if(len(self.res)>=k):
                pass
            else:
                self.res.append(node.val)

            DFS(node.right, k)

        DFS(root, k)
        print(self.res)

        return self.res[-1]
        
    
       
        