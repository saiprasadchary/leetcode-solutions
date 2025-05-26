# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.count=0
        def DFS(node):
            if node is None:
                return
            self.count+=1
            DFS(node.left)
            DFS(node.right)
        DFS(root)
        return self.count

        
        # que=deque()
        # que.append(root)
        # cnt=0
        # if root is None:
        #     return 0
        # while que:
        #     n=len(que)
        #     for i in range(n):
        #         node=que.popleft()
        #         cnt+=1
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        # return cnt
        