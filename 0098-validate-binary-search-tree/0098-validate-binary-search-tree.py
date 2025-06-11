# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        #we need to maintain the range for each and every node to detect the node's acceptance
        mini=float("-inf")
        maxi=float("inf")

        def dfs(node, mini, maxi):
            if node is None:
                return True
            if node.val<=mini or node.val>=maxi:
                return False
            return dfs(node.left, mini, node.val) and dfs(node.right, node.val, maxi)

        return dfs(root, mini, maxi)


        # if root is None:
        #     return True
        # self.prev=[]
        # self.flag=True

        # def BFS(node):
        #     que=deque()
        #     que.append(node)
        #     temp=[]
        #     flag=True
        #     while que:
        #         n=len(que)
        #         node=que.popleft()
        #         for i in range(n):
        #             if node.left:
        #                 if node.left.val>=node.val:
        #                     flag=False
        #                     break
        #                 que.append(node.left)
        #             if node.right:
        #                 if node.right.val<=node.val:
        #                     flag=False
        #                     break
        #                 que.append(node.right)
        #     return flag
        
        # return BFS(root)

           




                