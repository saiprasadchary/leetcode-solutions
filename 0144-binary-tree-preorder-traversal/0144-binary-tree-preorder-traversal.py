# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # using a stack 
        # res=[]
        # stack=[root]
        # if root is None:
        #     return res
        # while stack:
        #     node=stack.pop()
        #     res.append(node.val)
        #     #first comes right as we are using stack
        #     if(node.right):
        #         stack.append(node.right)
        #     if(node.left):
        #         stack.append(node.left)
        # return res

        # res=[]
        # if root is None:
        #     return res
        # def dfs(node):
        #     if(node==None):
        #         return
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return res

# another approach

    # def preorderTraversal(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     # Initialize the result list on the instance
    #     self.res = []
    #     # Kick off the real recursion
    #     self._preorder(root)
    #     return self.res
    
    # def _preorder(self, node):
    #     # Base case
    #     if node is None:
    #         return
    #     # Visit
    #     self.res.append(node.val)
    #     # Recurse left, then right
    #     self._preorder(node.left)

        res=[]
        node=root
        while node:
            if node.left is None:
                res.append(node.val)
                node=node.right
            else:
                curr=node.left
                while curr.right and curr.right!=node:
                    curr=curr.right
                # link is not yet established
                if curr.right is None:
                    curr.right = node
                    res.append(node.val)
                    node=node.left
                else:
                    #link is alreadily established
                    curr.right = None
                    node=node.right       
        return res





          

            
            

            
          


        