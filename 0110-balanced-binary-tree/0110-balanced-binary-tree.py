# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # I'll utilize the height of BT and manipualte its code to make it working for this
        
        #base case
        def check(node):
            if(node is None):
                return 0
            lh=check(node.left)
            rh=check(node.right)

            if(lh==-1 or rh==-1):
                return -1
            if(abs(lh-rh)>1): 
                return -1

            return 1+max(lh, rh)

        if check(root)!=-1:
            return True
        else:
            return False




        