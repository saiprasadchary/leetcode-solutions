# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution(object):
#     def postorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         # res=[]

#         # def DFS(node):
#         #     if node is None:
#         #         return
#         #     DFS(node.left)
#         #     DFS(node.right)
#         #     res.append(node.val)
#         # DFS(root)
#         # return res


#     def postorderTraversal(self, root):
#         self.res=[]
#         self.DFS(root)
#         return self.res

#     def DFS(self, node):
#         if(node is None):
#             return
#         self.DFS(node.left)
#         self.DFS(node.right)
#         self.res.append(node.val)


class Solution(object):
    def postorderTraversal(self, root):

        # using two stacks
        # st2=[]
        # res=[]
        # if root is None:
        #     return res
        # st1=[root]

        # while st1:
        #     node=st1.pop()
        #     st2.append(node)
        #     if(node.left):
        #         st1.append(node.left)
        #     if(node.right):
        #         st1.append(node.right)
        
        # while st2:
        #     res.append(st2.pop().val)
        # return res

# this approach is the reverse engineeering approach, and by manipulating the inorder traversal by taking right node till end and then going for left -> vice versa of inorder approach

 #-> first use the output and reverse it then the idea forms
        res=[]
        if root is None:
            return res
        stack=[]
        node=root
        while stack or node:
            if node is not None:
                stack.append(node)
                res.append(node.val)
                node=node.right
            else:
                node=stack.pop()
                node=node.left
        return res[::-1]


        
        