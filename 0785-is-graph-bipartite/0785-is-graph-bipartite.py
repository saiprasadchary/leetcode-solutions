class Solution(object):
    from collections import deque
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        ROWS=len(graph)
        if ROWS is None:
            return True
        visited=[-1]*ROWS

        for node in range(ROWS):
            if visited[node] !=-1:
                continue
            que=deque()
            que.append(node)
            visited[node]=0
            while que:
                curr=que.popleft()
                for neighbor in graph[curr]:
                    if visited[neighbor]==-1:
                        visited[neighbor]=1-visited[curr]
                        que.append(neighbor)
                    elif visited[neighbor]!=1-visited[curr]:
                        print(visited)
                        return False
        return True




        
        