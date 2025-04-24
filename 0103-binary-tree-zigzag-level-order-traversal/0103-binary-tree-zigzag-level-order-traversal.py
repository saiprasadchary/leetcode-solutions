# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        if root is None:
            return res
        
        que=deque()
        que.append(root)
        
        RightLeft=True

        while que:
            n=len(que)
            temp=[]
            for i in range(n):
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if(node.right):
                    que.append(node.right)
                temp.append(node.val)
            if(RightLeft):
                res.append(temp)
                RightLeft=False
            else:
                res.append(temp[::-1])
                RightLeft=True
        
        return res


        
        