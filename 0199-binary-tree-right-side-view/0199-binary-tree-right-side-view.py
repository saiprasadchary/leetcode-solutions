# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        # self.res=[]
        # level=0
        # def rightView(node, level):
        #     if node is None:
        #         return
            
        #     if(len(self.res)==level):
        #         self.res.append(node.val)
            
        #     rightView(node.right, level+1)
        #     rightView(node.left, level+1)
        
        # rightView(root, level)
        # return self.res

        if root is None:
            return []
        res=[]
        que=deque()
        que.append(root)
        while que:
            n=len(que)

            for col in range(n):
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(node.val)

        return res


        