# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if(root==None):
            return 0
        left=1+self.maxDepth(root.left)
        right=1+self.maxDepth(root.right)

        return max(left, right)

        # if root is None:
        #     return 0
        # que=deque()
        # cnt=0
        # que.append(root)
        # while que:
        #     n=len(que)
        #     cnt+=1
        #     for i in range(n):
        #         node=que.popleft()
        #         if(node.left):
        #             que.append(node.left)
        #         if(node.right):
        #             que.append(node.right)
        # return cnt
        