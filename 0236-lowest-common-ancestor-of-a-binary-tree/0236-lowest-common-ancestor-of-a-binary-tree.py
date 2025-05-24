# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        self.res1=[]
        self.res2=[]
        if root is None:
            return None

        def DFS(node, x, temp1):
            if node is None:
                return 
            temp1.append(node)
            if node == x:
                if not self.res1:
                    self.res1.extend(temp1) 
                else:
                    self.res2.extend(temp1)     
            else:
                DFS(node.left, x, temp1)
                DFS(node.right, x, temp1)
            temp1.pop()
      
        DFS(root, p, [])
        DFS(root, q, [])

        lca=0

        for pval, qval in zip(self.res1, self.res2):
            if pval == qval:
                lca=pval
            else:
                break
        return lca
