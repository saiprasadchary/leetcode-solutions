class Solution(object):

    # BFS solution:
    # from collections import deque
    # def isBipartite(self, graph):
    #     """
    #     :type graph: List[List[int]]
    #     :rtype: bool
    #     """
    #     ROWS=len(graph)
    #     if ROWS is None:
    #         return True
    #     visited=[-1]*ROWS

    #     for node in range(ROWS):
    #         if visited[node] !=-1:
    #             continue
    #         que=deque()
    #         que.append(node)
    #         visited[node]=0
    #         while que:
    #             curr=que.popleft()
    #             for neighbor in graph[curr]:
    #                 if visited[neighbor]==-1:
    #                     visited[neighbor]=1-visited[curr]
    #                     que.append(neighbor)
    #                 elif visited[neighbor]==visited[curr]:
    #                     return False
    #     return True

    #DFS solution:
    def dfs(self, node, col, graph, visited):
        visited[node]=col
        for neighbor in graph[node]:
            if visited[neighbor]==-1:
                if self.dfs(neighbor, 1-col, graph, visited)== False:
                    return False
            elif visited[neighbor]==col:
                return False
        return True

    def isBipartite(self, graph):
        ROW=len(graph)
        visited=[]
        for i in range(ROW):
            visited.append(-1)

        for i in range(ROW):
            if visited[i]==-1:
                if self.dfs(i, 0, graph, visited)== False:
                    return False 
        return True
        







        
        