# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        # Definition for a binary tree node.
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # I'll utilize the height of BT and manipualte its code to make it working for this
        
        #base case
        # def check(node):
        #     if(node is None):
        #         return 0
        #     lh=check(node.left)
        #     rh=check(node.right)

        #     if(lh==-1 or rh==-1):
        #         return -1
        #     if(abs(lh-rh)>1): 
        #         return -1

        #     return 1+max(lh, rh)

        # if check(root)!=-1:
        #     return True
        # else:
        #     return False

        def height_check(root):
            if root is None:
                return 0
            left=1+height_check(root.left)
            right=1+height_check(root.right)
            if(left==0 or right==0):
                return -1
            if abs(left-right)>1:
                return -1 # which inturn gets assigned to the upper level, either for the right or left
            return max(left, right)

        return height_check(root)!=-1
            


        




























        