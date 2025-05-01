from collections import deque, defaultdict

class Solution(object):
    def verticalTraversal(self, root):
        if root is None:
            return []
        
        # dict1 will map column index → list of (row, value)
        dict1 = defaultdict(list)
        min_col = max_col = 0
        
        # queue holds tuples: (node, column, row)
        que = deque([(root, 0, 0)])
        
        while que:
            node, col, row = que.popleft()
            
            # record this node’s row & value under its column
            dict1[col].append((row, node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            if node.left:
                que.append((node.left,  col - 1, row + 1))
            if node.right:
                que.append((node.right, col + 1, row + 1))
        
        # build the answer by iterating columns from leftmost to rightmost
        res = []
        for c in range(min_col, max_col + 1):
            # sort first by row, then by value
            column_nodes = sorted(dict1[c], key=lambda x: (x[0], x[1]))
            # extract just the node values
            res.append([val for _, val in column_nodes])
        
        return res