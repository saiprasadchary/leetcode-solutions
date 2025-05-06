# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        self.res=[]
        level=0

        def rightView(node, level):
            if node is None:
                return
            
            if(len(self.res)==level):
                self.res.append(node.val)
            print(self.res)
            
            rightView(node.right, level+1)
            rightView(node.left, level+1)

        rightView(root, level)
        return self.res

        