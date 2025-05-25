# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        que=deque()
        que.append((root,0))
        maxwidth=0
        
        while que:
            startq=que[0][1]
            endq=que[-1][1]
    
            maxwidth = max(maxwidth, endq-startq+1)
            n=len(que)
            
            for i in range(n):
                node, ind = que.popleft()
                if node.left:
                    que.append((node.left, 2*ind+1))
                if node.right:
                    que.append((node.right, 2*ind+2))

        return maxwidth


            

        