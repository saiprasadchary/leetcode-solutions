# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        self.list=[]
        def DFS(node):
            if node is None:
                return
            DFS(node.left)
            self.list.append(node.val)
            DFS(node.right)
        
        DFS(root)
        print(self.list)
        n=len(self.list)-1
        i=0
        while i<n:
            val=self.list[i]+self.list[n]
            if(val==k):
                return True
            elif(val<k):
                i+=1
            else:
                n-=1

        return False
          