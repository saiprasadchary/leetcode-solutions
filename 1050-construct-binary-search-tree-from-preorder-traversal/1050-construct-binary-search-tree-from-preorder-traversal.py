# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        n=len(preorder)
        maxbound=float("inf")
        self.pos=0
        if n==0:
            return None

        def Build(preorder, maxbound):
            if len(preorder)==self.pos or preorder[self.pos]>maxbound:
                return None

            val=preorder[self.pos]
            self.pos+=1

            root=TreeNode(val)
            root.left=Build(preorder, root.val)
            root.right=Build(preorder, maxbound)
            return root

        return Build(preorder, maxbound)
