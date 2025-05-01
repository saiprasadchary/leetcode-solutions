from collections import defaultdict, deque

class Solution(object):
    def verticalTraversal(self, root):
        if root is None:
            return []

        que = deque()
        que.append((root, 0, 0))  # (node, col, row)
        col_map = defaultdict(list)  # col -> list of (row, val)
        minCol, maxCol = 0, 0

        while que:
            node, col, row = que.popleft()
            col_map[col].append((row, node.val))
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if node.left:
                que.append((node.left, col - 1, row + 1))
            if node.right:
                que.append((node.right, col + 1, row + 1))

        result = []
        for col in range(minCol, maxCol + 1):
            # Sort by row first, then value if multiple nodes in same row
            entries = sorted(col_map[col], key=lambda x: (x[0], x[1]))
            result.append([val for row, val in entries])

        return result