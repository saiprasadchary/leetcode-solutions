# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack=[]
        self.left_push(root)

    def left_push(self, node):
        while node:
            self.stack.append(node)
            node=node.left

    def next(self):
        """
        :rtype: int
        """
        temp=self.stack.pop()
        val=temp.val
        if temp.right:
            self.left_push(temp.right)
        return val 

        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()