# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        #finding the parent of each and every node in the BT and storing in a dictionart for future use
        parent_dict={}
        def find_parent(node):
            if node is None:
                return
            if(node.left):
                parent_dict[node.left]=node
                find_parent(node.left)
            if(node.right):
                parent_dict[node.right]=node
                find_parent(node.right)
        #calling function
        find_parent(root)

        #BFS approach to solve it
        que=deque()
        que.append(target)
        visited=set()
        visited.add(target)
        
        while que and k:
            n=len(que)
            k-=1
            for i in range(n):
                node=que.popleft()
                #left
                if(node.left and node.left not in visited):
                    que.append(node.left)
                    visited.add(node.left)
                #right
                if(node.right and node.right not in visited):
                    que.append(node.right)
                    visited.add(node.right)
                #parent
                if node in parent_dict and parent_dict[node] not in visited:
                    que.append(parent_dict[node])
                    visited.add(parent_dict[node])
        
        return [node.val for node in que]








        