class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        # Helper function to find path from root to target node
        def findPath(node, target, path):
            if not node:
                return False
            path.append(node)
            if node == target:
                return True
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
            path.pop()
            return False

        path1, path2 = [], []

        # Find paths from root to p and q
        findPath(root, p, path1)
        findPath(root, q, path2)

        # Compare the two paths to find the last common node
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1

        return path1[i - 1] if i > 0 else None