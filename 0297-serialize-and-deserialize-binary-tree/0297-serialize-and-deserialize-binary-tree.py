# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        str_res=[]
        if root is None:
            return ""
        def DFS(node):
            if node is None:
                str_res.append("None")
                return
            str_res.append(str(node.val))
            DFS(node.left)
            DFS(node.right)
        DFS(root)
        return (",".join(str_res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        self.i=0
        preorder=data.split(",")
        def DFS():
            if preorder[self.i]=="None":
                self.i+=1
                return None
            root=TreeNode(int(preorder[self.i]))
            self.i+=1
            root.left=DFS()
            root.right=DFS()
            return root
        return DFS()
        
        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))