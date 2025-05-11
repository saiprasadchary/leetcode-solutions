# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return [] 
        que=deque()
        que.append(root)
        res=[]
  
        while que:
            
            loop_len=len(que)
            temp=[]
            for i in range(loop_len):
                node=que.popleft()
                temp.append(node.val)
                if(node.left):
                    que.append(node.left)
                if(node.right):
                    que.append(node.right)
                
            res.append(temp)
        return res

        